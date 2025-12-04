# Basisklasse
class Tier:
    def __init__(self, name):
        self.name = name

    def sprich(self):
        return "Ich bin ein Tier."

# Abgeleitete Klassen
class Hund(Tier):
    def sprich(self):
        return f"{self.name} sagt: Wuff!"

class Katze(Tier):
    def sprich(self):
        return f"{self.name} sagt: Miau!"

# Verwendung (Instanziierung)
if __name__ == "__main__":
    tiere = [
        Hund("Bello"),
        Katze("Minka"),
        Tier("Unbekannt")
    ]

    for tier in tiere:
        print(tier.sprich())
