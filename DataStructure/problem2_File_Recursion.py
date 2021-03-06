## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os


# # Let us print the files in the directory in which you are running this script
# print (os.listdir("./"))
#
# # Let us check if this file is indeed a file!
# print (os.path.isfile("./problem2_File_Recursion.py"))
# print (os.path.isdir("./testdir"))
#
# # Does the file end with .py?
# print ("./ex.py".endswith(".py"))


output = []


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    is_exist = os.path.isdir(path)
    if not is_exist:
        print("dir is not exist")
        return []
    file_name_list = os.listdir(path)
    for file_name in file_name_list:
        full_path = path + '/' + file_name
        if os.path.isfile(full_path) and file_name.endswith(suffix):
            output.append(full_path)
        elif os.path.isdir(full_path):
            output + find_files(suffix, full_path)
    return output


print('--- Test case 1 : search .c---')
print(find_files('.c', './testdir'))
output.clear()

print('--- Test case 2 : search .py---')
print(find_files('.py', '.'))
output.clear()

print('--- Test case 3 : ---')
print(find_files('.py', './testdir2'))
output.clear()

print('--- Test case 4 : ---')
print(find_files('.txt', './testdir'))

