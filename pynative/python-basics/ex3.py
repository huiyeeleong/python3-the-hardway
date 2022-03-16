# Use Python input() function to accept a string from a user.
# Calculate the length of string using the len() function
# Next, iterate each character of a string using for loop and range() function.
# Use start = 0, stop = len(s)-1, and step =2. the step is 2 because we want only even index numbers
# in each iteration of a loop, use s[i] to print character present at current even index number

userinput = input()

length = len(userinput)

for num in range(0, length - 1, 2):
    print(userinput[num])
