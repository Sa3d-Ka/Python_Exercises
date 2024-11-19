alpha = []
for i in range(97, 123):
    alpha.append(chr(i))
while True:
    x = input("Saisir une lettre: ").lower()
    if x in alpha:
        alpha.remove(x) 
        print(alpha)
    elif x != alpha:
        print("Deja suprimer")