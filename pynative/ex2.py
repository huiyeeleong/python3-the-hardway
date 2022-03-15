# Create a variable called previous_num and assign it to 0
# Iterate the first 10 numbers one by one using for loop and range() function
# Next, display the current number (i), previous number, and the addition of both numbers in each iteration of the loop. 
# At last, change the value previous number to current number ( previous_num = i).

previous_num = 0

print("Printing current and previous number sum in a range(10)")
for num in range(1,10):
    previous_num = num -1
    total = num + previous_num
    print(f"Current Number {num} Previous Number {previous_num} Sum: {total}" )    