# Creating Nested Dictionaries...........
student = {
    "name" : "Aniruddh Shamra",
    "score" : {
        "chem" : 97,
        "pty" : 96,
        "math" : 95
    }
}

print(student)

print(student["score"])

print(student["score"] ["chem"])