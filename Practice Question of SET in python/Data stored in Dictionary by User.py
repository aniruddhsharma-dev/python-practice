# Question : WAP to enter marks of 3 subject from the 
#            user and store them in a dictionary.


# Creating a empty dictionary........
marks = {}

# User input..........
user1 = int(input("Enter Sci marks : "))
user2 = int(input("Enter phy marks : "))
user3 = int(input("Enter math marks : "))

# Putting it into dictionary.........
marks.update({"sci" : user1})
marks.update({"phy" : user2})
marks.update({"math" : user3})

print(marks)