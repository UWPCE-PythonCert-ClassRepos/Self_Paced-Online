import os


def disp_cwd_files():
    """
    Print the full path for all files in the current directory
    """
    cwd = os.getcwd()
    for files in os.listdir():
        print(cwd+'/'+files)
    return


def copy_from_to(file_name, to_dir='/home/ndru/Documents/Self_Paced-Online/students/nDruP/'):
    """
    Copy a file from a source, to a destination
    w/o using shutil, or the OS copy command.
    """
    orig_file = open(file_name, 'rb')
    new_file = open(to_dir+'copy_'+file_name,'w+b')
    new_file.write(orig_file.read())
    new_file.close()
    orig_file.close()    
    return

    
disp_cwd_files()
copy_from_to('test.txt')
copy_from_to('test.jpg')
disp_cwd_files()
