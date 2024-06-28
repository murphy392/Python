import os, fnmatch

def match(folder, search):
    for filename in os.listdir(folder):
        if fnmatch.fnmatch(filename, search):
            print(filename)

match('./files', '*1*_file.csv')
