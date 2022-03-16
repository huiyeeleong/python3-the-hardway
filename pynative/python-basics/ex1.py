# Create a function that will take two numbers as parameters
# Next, Inside a function, multiply two numbers and save their product in a product variable
# Next, use the if condition to check if the product >1000. If yes, return the product
# Otherwise, use the else block to calculate the sum of two numbers and return it.

def number (num1 , num2):
    product = num1 * num2
    
    if product <= 1000:
        return product
    else:
        return num1 + num2

#Condition 1
result = number(20,30)
print(result) 

#Condition 2
result = number(40,30)
print(result)