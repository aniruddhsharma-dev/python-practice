# Making simple calculator...............................
print("simple calculator")
# taking user input...........................
num1 = float(input("Enter the First number : "))
num2 = float(input("Enter the Second number : "))
operator = input("Enter the operator (+, -, *, /,) : ")
# Printing the value assigned to variales ................
# print("1st number =",num1)
# print("2nd number =",num2)
# Applying Square and Cude Operation.................
if operator == "+":
    result = num1 + num2  # For Professional improvement..................
    print("Result = ",result)
elif  operator == "-":
    result = num1 - num2
    print("Result = ",result)
elif  operator == "*":
    result = num1 * num2
    print("Result = ",result)
elif  operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result = ",result)
    else:
        print("Cannot divided by zero")
else:
    print("Invalid Operator")