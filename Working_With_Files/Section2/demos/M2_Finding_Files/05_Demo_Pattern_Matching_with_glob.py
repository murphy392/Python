from pathlib import Path

def glob_match(fld, search):
    p = Path(fld)
    #search criteria is applied to the path.
    for n in p.glob(search):
        print(n)

# glob_match('./files', '*2*.t*')
glob_match('./files/subfolder', '*_file_*.t*')
