# Create a function that returns the sum of all numbers from 1 to n.

# Soltion:
def sum_of_numbers(n):           # Function for calculatiing the sum of number from 1 to n.
    total = 0                    # Intialize toal as 0.
    for i in range (1, n+1):     # For loop to get number from 1 to n and then add them to total.
        total += i               # adding a number to the total.
    return total
# Example usage:
print(sum_of_numbers(10))        # adding number from 1 to 10 and return the sum of numbers.