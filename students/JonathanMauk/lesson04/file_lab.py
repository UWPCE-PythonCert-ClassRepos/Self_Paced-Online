import os
import pathlib

for item in os.listdir():
    print(os.path.abspath(item))


def read_write(source, destination):
    with open(source, 'rb') as infile, open(destination, 'wb') as outfile:
        outfile.write(infile.read())
        infile.close()
        outfile.close()


read_write('source.txt', 'destination.txt')

print_source = open('source.txt', 'r')
print_destination = open('destination.txt', 'r')

print("Printing contents of 'source.txt...")
print(print_source.read())

print("Printing contents of 'destination.txt...")
print(print_destination.read())
