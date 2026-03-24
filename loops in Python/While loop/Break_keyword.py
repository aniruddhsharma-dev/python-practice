# Creating a program using Break keywoard.....
lis = [1, 2, 3, 4, 8, 6, 5, 7, 9, 22]

number = 6

# finding a number in list using while loop.......
i = 0
while i <= len(lis)-1:
    if (lis[i] == number):
        print("Number found at idx",i)
        break
    else:
        print("Finding....")
    i += 1

print("Loop ended")