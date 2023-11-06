from Contestant import Contestant

dictionary = {}

for i in range(10):
    dictionary[i] = "a"

for key in dictionary:
    print(dictionary[key])

empty_set = set()
contestant = Contestant("Remove this")
empty_set.add(contestant)

for i in range(9):
    empty_set.add(f"{i}")

print(f"Before: {empty_set}")
empty_set.remove(contestant)
print(f"After: {empty_set}")