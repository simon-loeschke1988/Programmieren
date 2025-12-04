class Tier:
    def __init__(self, name):
        self.name = name
    def rudel(self, anzahl_tiere):
        self.anzahl_tiere = anzahl_tiere    
        return f"{self.name} läuft im Rudel. Anzahl der Tiere im Rudel: {self.anzahl_tiere}"
    
class Hund(Tier):
    def bellen(self):
        return f"{self.name} bellt: Wuff Wuff!"
    
    def rudel(self, anzahl_tiere):
        return super().rudel(anzahl_tiere)
    
    
    
if __name__ == "__main__":
    hund1 = Hund("Rex")
    print(hund1.bellen())
    try:
        amount_of_dogs = int(input("Geben Sie die Anzahl der Hunde im Rudel ein: "))
        print(hund1.rudel(amount_of_dogs))
    except ValueError:
        print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
    
     
    
    