import os

directory = "./"

file_list = os.listdir(directory)

for filename in file_list:
        if(filename.startswith('_')):
                continue
        full_path = os.path.join(directory, filename)
        new_name = '_' + filename
        if(os.path.isfile(full_path)):
                os.rename(full_path, os.path.join(directory, new_name))
        elif(os.path.isdir(full_path)):
                os.rename(full_path, os.path.join(directory, new_name))
