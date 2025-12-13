import os
#create new file
try:
    with open("newfile.txt","x") as file: 
        file.write("this is newly created file ")
    print("file created succesfully")
except FileExistsError:
    print("file already exists")

# check if a file exists
filename = "sample.txt"
if os.path.exists(filename):
    print(f"the file exists.")
else:
    print(f"the file does not exists")

# create a new file if it does not exist
filename="date.txt"
if not os.path.exists(filename):
    with open(filename,"w")as file:
        file.write("this is a newly created file.\n")
    print("file was missing, so it has been created ")
else:
    print("file already exists ")                                    