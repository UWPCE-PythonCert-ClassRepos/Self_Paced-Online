#$ chmod +x dict_lab.py

#Lesson 04: File Lab
#Natalie Rodriguez
# March 31, 2018

def show_files():
    import pathlib
    pth = pathlib.Path('./')
    pth.is_dir()
    pth.absolute()
    for f in pth.iterdir():
                print(f)

show_files()

def copy_files(source, destination):
#copy file without using shutil, or OScopy
    with open(source, 'rb') as f_source:
        with open(destination, 'wb') as f_destination:
            for data in f_source:
                f_destination.write(data)

copy_files(r'C:\Users\natstr8\Desktop\DSC_0183.jpg', r'C:\Users\natstr8\Desktop\Python\Testing')
copy_files(r'C:\Users\natstr8\Desktop\Writing_Sample_Assessment.docx', r'C:\Users\natstr8\Desktop\Python\Testing')