import os, sys

# Directory
directory = "test_dir"

# Path to parent directory
parent_dir = "C:/Users/Miskeen/OneDrive/Documents/github/tech257_python/scripting/os_module"

# Path
path = os.path.join(parent_dir, directory)

# Filename and path
filename = "testfile.txt"
filepath = os.path.join(path, filename)

# Make the file
with open(filepath, "w") as file1:
    toFile = "Contents of the file are here"
    file1.write(toFile)
print(f"File {filename} created in {directory}")
