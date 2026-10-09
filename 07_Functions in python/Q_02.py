# WAP to print the element of a list in a single line.(lit is paramenter)
marks = [52,63,41,45,63,21,78,90]
names = ["rahul", "ravi", "krish", "ram ji"]

def print_list(list):
    for item in list:
        print(item, end = " ")

print_list(names)
print_list(marks)