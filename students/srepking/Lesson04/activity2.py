import os
# Write a program which prints the full path for all files in the current directory, one per line.
complete_path= os.getcwd()
files=os.listdir(complete_path)
for f in files:
    print(complete_path+"\\"+f)

# Write a program which copies a file from a source, to a destination)
with open('input.txt', 'r') as from_file, open('output.txt', 'w') as to_file:
    clipboard = from_file.read()
    to_file.write(clipboard)