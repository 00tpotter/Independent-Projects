import cx_Freeze

executables = [cx_Freeze.Executable("Word Search Game.py")]

cx_Freeze.setup(
    name="Word Search Game",
    options={"build_exe": {"packages":["pygame", "random", "numpy", "copy", "sys"],
                           "include_files":["words.txt", "high_score.txt"]}},
    executables = executables

    )
