import os
import shutil

home = os.getenv('HOME')
from_dir = f'{home}/Downloads/'
to_dir = f'{home}/Downloads/documents'

list_of_files = os.listdir(from_dir)
print(f"Moving files from {from_dir} to {to_dir}")

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension == " ":
        continue 
    if extension in ['.txt', '.doc','.docx','.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = from_dir + '/' + "Image Files"
        path3 = from_dir + '/' + "Image Files" + '/' + file_name


        if os.path.exists(path2):
            print("Moving " + file_name + "...")

            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Moving " + file_name + "...")
            shutil.move(path1, path3)

print("Done!")        
        
