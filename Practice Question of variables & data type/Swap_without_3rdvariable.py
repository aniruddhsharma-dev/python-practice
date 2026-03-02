# Swaping of two numbers without using 3rd variable...............................

print("Swaping of two numbers")
# taking user input...........................
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
# Printing the value assigned to variales................
print("Before swapping:")
print("a = ",a)
print("b = ",b)
# Applying Square and Cude Operation.................
a, b = b, a
print("After swapping:")
print("a = ",a)
print("b = ",b)
