# Write a program to remove characters from a string starting from zero up to n and return a new string.

# For example:
# remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
# remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.

# Use string slicing to get the substring. For example, to remove the first four characters and the remeaning use s[4:].

def slice (char, num):
    x = char[num:]
    return x

print(slice("pynative",2))
print(slice("pynative",4))