
"""Get a little bit of practice with handling files and parsing simple text"""

# Write a program which prints the full path for all files in the current directory, one per line
import pathlib
pth = pathlib.Path('./')
for f in pth.iterdir():
    print(f)


# Write a program which copies a file from a source, to a destination
def copy_file(the_filename, destination):
    with open(the_filename, 'rb') as infile, open(destination, 'wb') as outfile:
        outfile.write(infile.read())
