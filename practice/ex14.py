def list_alter(list):
    b = []
    for i in list:
        if i in list:
            if i not in b:
                b.append(i)
    return b


a = [1, 2, 3, 4, 3, 2, 1]
print(list_alter(a))
