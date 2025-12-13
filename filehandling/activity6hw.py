import os
filename = "newfile.txt"
if os.path.exists(filename):
    os.remove(filename)
    print(f"file'{filename}' deleted succesfully")
else:
    print(f"file'{filename}'does not exists") 

folder_name = "test_folder"
if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"folder'{folder_name}' deleted succesfully")
else:
    print(f"folder'{folder_name}'does not exists")               



