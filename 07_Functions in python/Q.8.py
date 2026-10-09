# Write a function to find the maximum of two numbers.

# Solution:
num1 = int(input("Enter the first number: ")) # Taking input from the user and converting it to an integer
num2 = int(input("Enter the second number: ")) # Taking input from the user and converting it to an integer

# Defining a function to find the maximum of two numbers
def max_of_two_numbers(num1,num2):
    if (num1 > num2):                               # Comparing the two numbers and returning the largest one
        return (f"{num1} is the largest") 
    elif (num2 > num1):                             # Comparing the two numbers and returning the largest one
        return (f"{num2} is the largest") 
    else:
        return "Both numbers are equal"

result =max_of_two_numbers(num1,num2)  # Calling the function with the user input and storing the result in a variable
print(result) # Calling the function and printing the result