def find_indices(string2):
    string1="Hello coders to welcome to new coders guidlenes, here you will meet new coders"
    indices = []
    index = string1.find(string2)

    while index != -1:
        indices.append(index)
        index = string1.find(string2, index + 1)

    if len(indices) == 0:
        return -1
    else:
        return indices

# Test the function
print(find_indices("coders")) #output=[6,31,72]
