import os

files = os.listdir()
working_dir = os.getcwd()

for file in files:
    print(os.path.join(working_dir, file))