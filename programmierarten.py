#prozessuale programmierart

a = 4
b = 5

if a > b :
    print( "das ist grösser")
    

#funktionale programmierung

def vergleich():
    a = 4
    b = 5
    if a > b:
        return "das ist grösser"
    
vergleich()


#objektorientierte programmierung

class Vergleich:
    def __init__(self,a=4,b=5):
        self.a=a
        self.b=b
    def vergleich(self):
        if self.a > self.b:
            return "das ist grösser"
        
