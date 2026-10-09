# Create a function that checks if a number is even or odd.

# Solution:
intput_number = int(input("Enter a number: ")) # Taking input from the user and converting it to an integer
# Function to check if the number is even or odd
def check_even_dd(intput_number): # The function takes an integer as input and checks if it is even or odd
    if (intput_number % 2 ==0):   # If the number is divisible by 2, it is even
        return "EVEN"             # If the number is not divisible by 2, it is odd
    else:                         # If the number is not divisible by 2, it is odd
        return "ODD"
# Calling the function and printing the result
result = check_even_dd(intput_number) 
print(f"The number is: {result}") # Output will be either "EVEN" or "ODD" based on the input number.