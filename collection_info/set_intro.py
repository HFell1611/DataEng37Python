mcu = {"Iron Man", "Thor", "Captain America", "Hulk"}

print(mcu, type(mcu))
# Sets are unordered

mcu.add("Hawkeye")
mcu.add("Black Widow")

# print(mcu)
# print(mcu.pop())

mcu.discard("Iron Man")
print(mcu)

mcu.add("Thor")
print(mcu)

nums = [1, 3, 4, 5, 2, 6, 2, 4, 5, 12, 4, 1, 43]
print(nums)
print(list(set(nums)))  # Removes duplicates


# Frozen Set

fs = frozenset(nums)  # IMMUTABLE
print(fs, type(fs))
