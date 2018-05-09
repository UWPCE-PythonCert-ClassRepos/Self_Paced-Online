#Lesson 4 File Lab

def list_files():
    """Print file names in current dir"""
    import os
    for cur_file in os.listdir():
        print(cur_file)
        

def copy_file(source, dest):
    """Copy file to new location"""
    with open(source, 'rb') as in_file, open(dest, 'wb') as out_file:
        while True:
            file_chunk = in_file.read(4096)
            if not file_chunk:
                break
            out_file.write(file_chunk)
            
            
            
 
    
