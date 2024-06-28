import os

"""check the file extension"""
def ends_with(fld, search):
    for fn in os.listdir(fld):
        if fn.endswith(search):
            print(fn)


"""check the beginning of the file name"""
def starts_with(fld, search):
    for fn in os.listdir(fld):
        if fn.startswith(search):
            print(fn)

#ends_with('./files', '.txt')
starts_with('./files', '01_test')
