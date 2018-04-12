


import os


for dir in os.listdir():
    print(dir)



with open('/home/roy/Pictures/Selection_001.png', 'rb') as f:
    copy_file = open('copy_file', 'wb')
    for line in f.readlines():
        copy_file.write(line)


