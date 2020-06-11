# *************************************************
#                 SpotifyPlayer.py
#
# Description:  Auto DJ program that adds songs to
#               your queue automatically. Utilizes
#               a QR code linked to a Google Form
#               that accepts a song title and
#               artist.
# 
# Requirements: Access to the Spotify API, Google
#               Drive API, and Google Sheets API,
#               an instance of Spotify open and
#               playing a song
#
# Dependencies: SpotifyCredentials.txt,
#               client_secret.json,
#               SpotifyPlayer (Responses)
#
# Execution:    python SpotifyPlayer.py (username)
# 
# Author: Teddy Potter
# *************************************************

import sys
import spotipy
import spotipy.util as util
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import threading
from notify_run import Notify

# setting up phone notifications
notify = Notify()

# setting the scopes for the two APIs
spotScope = 'streaming'     # scope so that I can access my current queue
spreadScope = ['https://spreadsheets.google.com/feeds',
               'https://www.googleapis.com/auth/drive']

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

# credentials for Spotify API, read them in from a text file
text_file = open("SpotifyCredentials.txt", "r")
ids = text_file.read().splitlines()

token = util.prompt_for_user_token(username, spotScope, client_id = ids[0], client_secret = ids[1], redirect_uri = ids[2])

# credentials for Google Drive API
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', spreadScope)
client = gspread.authorize(creds)

# get the correct sheet
sheet = client.open("SpotifyPlayer (Responses)").sheet1

count = 0   # count of current songs added

songs_added = []    # list to keep track of the songs already added, used to avoid duplicates

# main function to add songs to the queue
# the reason it is a function is so that I can use threading to call it every 5 seconds
def add():
    if token:
        sp = spotipy.Spotify(auth=token)
        list_of_songs = sheet.get_all_records()
        length = len(list_of_songs) # the amount of songs in the spreadsheet

        global count    # global so that count is consistent across threads
        if count < length:
            song = list_of_songs[count]['Song title']
            artist = list_of_songs[count]['Artist name']
            query = 'track:' + song + ' artist:' + artist   # query formatting to prioritize track name and then artist
            
            # if artist is empty, just search for the song title
            if artist == '':
                query = 'track:' + song

            song_to_add = sp.search(query, limit=1, offset=0, type='track', market=None)    # running a search in spotify

            # getting the track uri from the search results (it returns a whole bunch of stuff)
            track = song_to_add['tracks']['items']
            global songs_added  # global to remain consisten across threads

            # need to make sure the search returned something, so track cannot be empty
            # avoid adding duplicates, so track cannot have already been added
            if track and not track[0]['uri'] in songs_added: 
                uri = track[0]['uri']   # uri that is able to be added to the queue in spotify  
                sp.add_to_queue(uri, device_id=None)    # add the song to the current queue
                songs_added.append(uri) # add song to list of songs already added

            # if the search didn't return anything, then send a phone notification 
            elif not track:
                message = query + " not found"
                notify.send(message)

            # if the song was already added, send a phone notification
            elif track[0]['uri'] in songs_added:
                message = query + " already in queue"
                notify.send(message)

            count += 1
            
    else:
        print("Can't get token for", username)

    threading.Timer(5, add).start()     # create a thread every 5 seconds that runs the function

print("Running... (ctrl+C or ctrl+pause to end)")
add()