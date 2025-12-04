
"""
    Aufgabe: Fahrzeugverwaltung
Erstelle ein Programm, das eine Fahrzeugverwaltung simuliert. Dazu sollen folgende Klassen implementiert werden:

Klasse Fahrzeug:

Attribute:
marke (z. B. "BMW", "Audi")
baujahr (z. B. 2020)
Methoden:
beschreibung(): Gibt eine Beschreibung des Fahrzeugs zurück, z. B. "BMW, Baujahr 2020".

Klasse Auto (erbt von Fahrzeug):

Zusätzliche Attribute:
anzahl_tueren (z. B. 3 oder 5)
Methoden:
Überschreibe die Methode beschreibung(), um auch die Anzahl der Türen anzugeben, z. B. "BMW, Baujahr 2020, 5 Türen".

Klasse Motorrad (erbt von Fahrzeug):

Zusätzliche Attribute:
hubraum (z. B. 600 für 600ccm)
Methoden:
Überschreibe die Methode beschreibung(), um auch den Hubraum anzugeben, z. B. "Yamaha, Baujahr 2018, 600ccm".

Klasse Fahrzeugverwaltung:
Attribute:
fahrzeuge (eine Liste, die alle Fahrzeuge speichert)
Methoden:
hinzufuegen(fahrzeug): Fügt ein Fahrzeug zur Liste hinzu.
alle_fahrzeuge_anzeigen(): Gibt die Beschreibung aller gespeicherten Fahrzeuge aus.
Anforderungen:
Erstelle mindestens ein Objekt der Klasse Auto und ein Objekt der Klasse Motorrad.
Füge diese Objekte zur Fahrzeugverwaltung hinzu.
Gib alle Fahrzeuge in der Fahrzeugverwaltung aus.
"""

class Fahrzeug:
    def __init__(self,marke,baujahr):
        self.marke=marke
        self.baujahr=baujahr
    
    def beschreibung(self):
        return  f"{self.marke}, {self.baujahr}"
   
    

class Auto(Fahrzeug):
    def __init__(self,anzahl_tueren,baujahr,marke):
        super().__init__(baujahr,marke)
        self.anzahl_tueren = anzahl_tueren
    def beschreibung(self):
        return f"{self.marke}, {self.baujahr}, {self.anzahl_tueren}"
        
    

class Motorrad(Fahrzeug):
    def __init__(self,hubraum,baujahr,marke):
        super().__init__(baujahr,marke)
        self.hubraum = hubraum
    def beschreibung(self):
        return f"{self.marke}, {self.baujahr}, {self.hubraum}"

class Fahrzeugverwaltung:
    def __init__(self):
          self.fahrzeuge = []
        
    def hinzufuegen(self,fahrzeug):
        self.fahrzeuge.append(fahrzeug)
    
    def alle_fahrzeuge_anzeigen(self):
        for fahrzeug in self.fahrzeuge:
            print(fahrzeug.beschreibung())


if __name__ == "__main__":
        auto = Auto(4,1999, "VW")
        motorrad = Motorrad(75,1999,"Harley")
        verwaltung = Fahrzeugverwaltung()
        
        #print(auto.beschreibung())
        verwaltung.hinzufuegen(auto)
        verwaltung.hinzufuegen(motorrad)
        verwaltung.alle_fahrzeuge_anzeigen()
        