#Was ist denn eine Klasse?

class Auto:
    def __init__(self,marke,modell,unfallfrei,baujahr="1999"):
        self.marke=marke
        self.modell=modell
        self.unfallfrei=unfallfrei
        self.baujahr=baujahr
    
    def hupen(self):
        return "Hup Hup!"
    
    #Abstrakte Methode:
    def beschleunigung(self,baujahr):
        pass

# Latein: super = "übergeordnet", sub = "untergeordnet"

class Oldtimer(Auto):
    def beschleunigung(self,baujahr):
        print(super().baujahr)
        super().hupen()
        return "Oldtimer beschleunigt langsam."
    
class Rennwagen(Auto):
    def beschleunigung(self):
        print(super().hupen())
        return "Rennwagen beschleunigt sehr schnell."





if __name__=="__main__":
    
    # Liste von autos als array:
    
    auto1=Auto("VW","Golf",True)
    Oldtimer1=Oldtimer("Ford","Model T",False)
    Rennwagen1=Rennwagen("Ferrari","488 GTB",True)
    print(Rennwagen1.beschleunigung())
    print(Oldtimer1.beschleunigung())
    print(f"Oldtimer 1: {Oldtimer1.marke}, {Oldtimer1.modell}, Unfallfrei: {Oldtimer1.unfallfrei}")
    
    print(Rennwagen1.hupen())

    print(f"Rennwagen 1: {Rennwagen1.marke}, {Rennwagen1.modell}, Unfallfrei: {Rennwagen1.unfallfrei}")
    print(f"Auto 1: {auto1.marke}, {auto1.modell}, Unfallfrei: {auto1.unfallfrei}")
    