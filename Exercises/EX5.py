def main():
    ahmad_notes , ahmad_matier = remplissage("Ahmed")
    khalid_notes, khalid_matier = remplissage("Khalid")

    moyenne_ah = moyenne_general(ahmad_notes)
    moyenne_kh = moyenne_general(khalid_notes)


    bulletin("Ahmed", ahmad_matier, ahmad_notes, moyenne_ah)
    bulletin("Khalid", khalid_matier, khalid_notes, moyenne_kh)


    plus_grand(moyenne_ah, moyenne_kh)





def remplissage(nom):
    notes = []
    matiers =[]
    Nm = int(input(f"{nom}, Combient des matiers? "))
    for _ in range(Nm):
        while True:
            matier = input("Entrer la matier: ")
            if matier in matiers:
                print("Matière est déjà existante. Réessayez.")
            else:
                break
        matiers.append(matier)
        while True:
            try:
                note = float(input("Entrer les notes: "))
                if 0 <= note <= 20:
                    notes.append(note)
                    break
                else:
                    print("La Note est incorrect, Répeter")
            except ValueError:
                print("La Note est incorrect, Répeter")
    return notes, matiers


def moyenne_general(notes):
    if len(notes) == 0:
        return 0
    moy = sum(notes) / len(notes)
    return moy


def bulletin(nom, matiers, notes, moyenne):
    print(f"{'-' * 10} {nom} {'-' * 10}")
    for i in range(len(matiers)):
        print(f"{matiers[i]}: {notes[i]}")
    print("-" * 20)
    print(f"Moyenne general: {moyenne:.2f}\n")


def plus_grand(moyenne_ah, moyenne_kh):
    if moyenne_ah > moyenne_kh:
        print("Ahmed a la plus grande moyenne.")
    elif moyenne_ah < moyenne_kh:
        print("Khalid a la plus grande moyenne.")
    else:
        print("Ahmed et Khalid ont la meme moyenne.")

main()