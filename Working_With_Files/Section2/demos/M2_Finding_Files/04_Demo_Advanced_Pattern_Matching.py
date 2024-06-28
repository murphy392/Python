import os, fnmatch

def match(folder, search):
    for fn in os.listdir(folder):
        if fnmatch.fnmatch(fn, search):
            print(fn)

#match('./files', '*_file*.*')
#match('./files', '*_file_*.*')
match('./files', '*2_*_*.*')
