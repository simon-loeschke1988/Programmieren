//if, if ... else, else if

var liste = ["Banane", "Apfel", "Birne", "Bär", "Katze", "Maus"]; // Array

// Werte aus Variablen mit verschiedenen Datentypen ausgeben:

var nutzereingabe1 = prompt("Rate die Länge der Liste!");

if (nutzereingabe1 != liste.length) {
  console.log("Falsch gelegen ");
  var nutzereingabe1 = prompt("Nochmals eingeben: ");
  console.log("Vor der if-Abfrage:" + liste.length);
  if (nutzereingabe1 == liste.length) {
    console.log("nach der if-schleife: Nutzereingabe: " + nutzereingabe1);
    console.log("Und die Listenlänge: " + liste.length);
    console.log("Richtig! Gewonnen");
  } else {
    console.log("Du hast verloren!");
  }
}
