import difflib

# Function to read the text files
def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

# File paths
file1 = 'vanburencountymi_564.txt'
file2 = 'vanburencountymi_buildings_grounds.txt'

# Read the contents of the files
text1 = read_file(file1)
text2 = read_file(file2)

# Compare the files and generate the diff
diff = difflib.unified_diff(text1, text2, fromfile='vanburencountymi_564.txt', tofile='vanburencountymi_buildings_grounds.txt')

# Print the differences
for line in diff:
    print(line)