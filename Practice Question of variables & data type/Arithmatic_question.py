# Take two numbers from user and print their:
# Sum
# Difference
# Multiplication
# Division

print("Take two numbers from user and print their :\nSum\nDifference\nMultiplication\nDivision")
# taking user input
a = int(input("Enter the First number : "))
b = int(input("Enter the Second number : "))
# Printing the value assigned to variales 
print("a =",a)
print("b =",b)
# Applying Arithmatic operators
# Addition of Two numbers
sum_ = a + b
# Substrication of two numbers
Sub = a - b
# Multiplication of two numbers
multi = a * b
#Division of Two numbers
if b !=0:
    div = a/b
    print("division = ",div)
else:
    print("Cannot be divided by zero")

#Printing the final output
print("The Addition of Two numbers is :",sum_)
print("The Substraction of Two numbers is :",Sub)
print("The Multiplication of Two numbers is :",multi)
