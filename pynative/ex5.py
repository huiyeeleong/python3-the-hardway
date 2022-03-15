# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

def num (numberlist):
    numberx = numberlist[0]
    numbery = numberlist[-1]
    
    if numberx == numbery:
        return True
    else:
        return False
    
numbers_x =  [10, 20, 30, 40, 10]

print(num(numbers_x))