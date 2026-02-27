name = input("Enter your name : ")
age = int(input("Enter your age :"))

print(f"Welcome {name}")
print(f"You are {age} years old.")

if age >= 18:
    if age <= 70:
        print("Yoy can drive")
    else:
        print("You cannot drive")
else:
    print("You cannot drive")