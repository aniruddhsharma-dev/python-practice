# Finding Leap year...........
year = int(input("Enter a year : "))

# printing the year user has given...............
print(f"You have given {year} to check thia is a leap year or not.") # used F-String in it.


if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is a not leap year")