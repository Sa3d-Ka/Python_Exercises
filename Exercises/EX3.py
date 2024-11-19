list = []

for i in range(5):
    x = input("Remplir la list: ")
    list.append(x)
print(list)

list[0], list[-1] = list[-1], list[0]

print(list)