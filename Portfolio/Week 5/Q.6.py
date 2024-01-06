'''Write a program that takes the name of a file as a command-line argument, and
creates a backup copy of that file. The backup should contain an exact copy of the
contents of the original and should, obviously, have a different name.
Hint: By now, you should be getting the idea that there is a built-in way to do the
heavy liing here! Take a look at the "Brief Tour of the Standard Library" in the docs.'''

import sys
import shutil

def copy_file(file_name):
    '''Copy file from one file to another.'''
    shutil.copyfile(file_name, 'destination.txt')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid input")

    else:
        file_name = sys.argv[1]
    
    copy_file(file_name)

