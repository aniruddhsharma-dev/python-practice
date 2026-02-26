Amount = int(input("Enter a amount : "))
print("Amount = ",Amount)

notes_500 = Amount // 500
Amount1 = Amount % 500

notes_200 = Amount1 // 200
Amount2 = Amount1 % 200

notes_100 = Amount2 // 100
Amount3 = Amount2 % 100

print("500 notes = ",notes_500)
print("200 notes = ",notes_200)
print("100 notes = ",notes_100)