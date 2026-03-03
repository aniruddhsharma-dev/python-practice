# Creating a Dictionary............
info = {
    "name" : "Aniruddh Sharma",
    "CGPA" : 9.6,
    "marks" : [98, 97, 95],
    "age" : 19,
    "is_adult" : True,
    1 : "neelam",
    1.2 : "Vinod",
}

# Nested Dictionaries.................
student = {
    "name" : "Aniruddh Shamra",
    "score" : {
        "chem" : 97,
        "pty" : 96,
        "math" : 95
    }
}

# .Key() Dictionary method.............
print(list(info.keys()))
print(len(info))
print(" ")
# .Key() Nested Dictionary method.............
print(list(student.keys()))
print(len(student))

print(" ")

# .Values() Dictionary method...........
print(list(info.values()))
# .Values() Nested Dictionary method...........
print(list(student.values()))

print(" ")

# .Items() Dictionary method............
print(info.items())
# .Items() Nested Dictionary method...........
print(student.items())
# For printing a specific pair...............
pairs = list(info.items())
print(pairs[3])
# For printing a specific pair in nested Dictinory...............
pairs = list(student.items())
print(pairs[1])



# .get() Dictionary method...............
print(info.get("name"))
# .get()nested Dictionary method...............
print(student.get("score"))



# .update() Dictionary method..............
info.update({"City" : "Indore"})
print(info)
new_dict = {"State" : "M.P."}
info.update(new_dict)
print(info)