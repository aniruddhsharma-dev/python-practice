# WAP to retun string "Odd" and "Even"
num = int(input("Enter a number : "))

# Function define....
def string_ret(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(string_ret(num))