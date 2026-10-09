# Write a function to return the square of a number.

# Solution:
num = int(input("Enter a number: ")) # Taking input from the user
def square(num):
    return num ** 2 # Returning the square of the number
result = square(num) # Calling the function and storing the result
print(f"The square of the number {num} is: {result}") # Printing the result