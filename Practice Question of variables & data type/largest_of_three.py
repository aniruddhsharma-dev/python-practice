# Largest of Three numbers...............................

print("Finding the largest of three numbers")
# taking user input...........................
num1 = int(input("Enter the First number : "))
num2 = int(input("Enter the Second number : "))
num3 = int(input("Enter the Third number : "))
# Printing the value assigned to variales ................
print("1st number =",num1)
print("2nd number =",num2)
print("3rd number =",num3)
# Applying Square and Cude Operation.................
if num1 >= num2 and num1 >= num3:
    print(f"Number {num1} is the largest")
elif num2 >= num1 and num2 >= num3:
    print(f"Number {num2} is the largest")
else:
    print(f"Number {num3} is the largest")
