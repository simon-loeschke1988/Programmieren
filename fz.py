
class Fahrzeugverwaltung:
    def __init__(self):
        self.fahrzeuge = []  # Liste zur Speicherung von Fahrzeugen
    
    def hinzufuegen(self, fahrzeug):
        self.fahrzeuge.append(fahrzeug)  # Fahrzeug zur Liste hinzufügen
    
    def alle_fahrzeuge_anzeigen(self):
        for fahrzeug in self.fahrzeuge:
            print(fahrzeug.beschreibung())  # Beschreibung jedes Fahrzeugs ausgeben