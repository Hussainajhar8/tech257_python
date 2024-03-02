import os, sys

# Directory
directory = "TEST_dir"

# Path to parent directory
parent_dir = "C:/Users/Miskeen/OneDrive/Documents/github/tech257_python"

# path
path = os.path.join(parent_dir, directory)

os.mkdir(path)