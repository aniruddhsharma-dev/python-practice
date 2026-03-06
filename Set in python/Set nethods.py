# Creating a set...........
Collectiion = {"Aniruddh", "Ravi", "Kishan", "Rahul"}
print(Collectiion)

# Adding an element in set...........
Collectiion.add("Karan")
print(Collectiion)


# Removeing An element from Set............
Collectiion.remove("Ravi")
print(Collectiion)


# Removing a random value from set..............
Collectiion.pop()
print(Collectiion)


# Removing all the elements of set...........
Collectiion.clear()
print(Collectiion)


# Union (Combining) two sets.............
set1 = {1,2,3,4,5}
set2 = {2,4,6,7,8,}
print(set1.union(set2))


# Intersection the common elements in the set........
set1 = {1,2,3,4,5}
set2 = {2,4,6,7,8,}
print(set1.intersection(set2))