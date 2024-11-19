import random
T = []

for i in range(1, 11):
    T.append(random.randrange(1, 11))  
for element in T:
    if element % 2 == 0:
        index = T.index(element)
        print(f"{element} de position {index}")