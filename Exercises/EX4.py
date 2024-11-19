from datetime import datetime

def main():
    while True:
        try:
            retard = calcule_retard()
            amende(retard)
        except EOFError:
            break
        except KeyboardInterrupt:
            break


def calcule_retard():
    
    date_prevue = input("Entrer la date de retour prévue (DD/MM/YYYY): ")
    date_reel = input("Entrer la date réel de retour (DD/MM/YYYY): ")

            
    prevue = datetime.strptime(date_prevue, "%d/%m/%Y")
    reel = datetime.strptime(date_reel, "%d/%m/%Y")

            
    retard = (reel - prevue).days
    return retard


def amende(retard):
    if retard > 0:
        amende = retard * 5
        print(f"Le retard: {retard} jours")
        print(f"L'amende: {amende} Dh")
    else:
        print("Aucun retard, aucune amende.")


main()