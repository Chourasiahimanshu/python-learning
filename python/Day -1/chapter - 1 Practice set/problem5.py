import os
# specify the directory path you want to list
directory_path = '/' 

# list all files and directories in the specified path
contents = os.listdir(directory_path)

# print each item in the contents and directory path
for item in contents:
    print(item)