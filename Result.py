# Student marks distribution...............................
print("Students marks distribution")
# taking user input...........................
name = input("Enter student name : ")
eng = float(input("Enter English marks : "))
math = float(input("Enter Math marks : "))
science = float(input("Enter Science marks : "))
so_sce = float(input("Enter so_sce marks : "))
Evs = float(input("Enter EVS marks : "))
# Printing the value assigned to variales ................
# print("English marks =",eng)
# print("Maths marks =",math)
# print("Science marks =",science)
# print("So_sce marks =",so_sce)
# print("Evs marks =",Evs)
# Applying Square and Cude Operation.................
Total = (eng+math+science+so_sce+Evs)/(500) * 100 
print("Total = ",Total)

if Total >= 90:
    print("Grade = A")
elif  Total <= 89 and Total >= 75:
    print("Grade = B")
elif  Total <= 74 and Total >= 50:
    print("Grade = C")
elif  Total <= 49 and Total >= 30:
    print("Grade = D")
else:
    print("Fail")