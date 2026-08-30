import os

directory_path = '/' 

# Print the contents of the current directory
contents = os.listdir(directory_path)

for item in contents:
    print(item)