print("STUDENTS MARKSHEET")

name = input("Enter your name : ")
total_marks = int(input("Enter student's marks : "))

print(f"Mark Sheet of {name}.")
print(f"Total marks of {name} out-of 100 = {total_marks}.")

if total_marks >= 90:
    print("Grade = A")
elif total_marks >= 75:
    print("Grade = B")
elif total_marks >= 65:
    print("Grade = C")
elif total_marks >= 55:
    print("Grade = D")
elif total_marks >= 35:
    print("Grade = E")
else:
    print("FAIL")