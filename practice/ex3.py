a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
check = input("Please pick a number:\n")
check_int = int(check)
# for i in a:
#     if i < 5:
#         print(i)

# for i in a:
#     if i < 5:
#         b.append(i)
#
# for x in b:
#     print(x)


for i in a:
    if i < check_int:
        b.append(i)

print(b)
