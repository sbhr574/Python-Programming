name = "Subhajit Roy"
print(name[1:4])
print(name[:4])
print(name[2:])

# Negative Index slicing
place = "Bengaluru"
print(place[-3:-1])

# Functions
line = "I am learning python from youtube"
print(line.endswith("youtube"))
print(line.endswith("you"))

print(line.replace("python", "JS"))
print(line.find("from"))  # first character or word will find from the string
print(line.find("z"))  # will return -1 because it's not available
