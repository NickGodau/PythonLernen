from tkinter import * # Import Libaries
name = "Nick" #Variable mit Namen
surename = "Godau"
alter = 19 # Variable mit Zahl
print(name, surename, alter) #Ausgabe in Konsole
name_external = input("Bitte geben Sie Ihren Namen ein") #Etwas aus der Konsole auslesen und in eine Variable speichern
print(name_external)
zahl1 = input("Bitte Zahl eingeben") #Speichert die Zahl als Text
zahl2 = int (input("Bitte Zahl eingeben")) #Speichert die Variable als Integer Zahl
print("2 + 3 + 4") #String Ausgabe
print (eval("2 + 3 + 4 ")) #String evaluiert 

#Python Datentypen #Python Datentypen
#Python Datentypen #Python Datentypen
#Python Datentypen #Python Datentypen

var1 = None
print(var1)
var1 = "Text"
print(var1)
var2 = True #bool
var3 = False # oder boolean
print(var2)
print(var2 + 1)
var4 = 1 #int
var5 = 1.0 #float
print(var5)
var6 = 1 + 4j #real + imaginärteil, j = imaginär
var7 = "Stringt"
var8 = 'oder String'
var9 = 'oder mit Zeilenumbruch\n kann passieren'
var10 = 7
print(type(var10)) #Bestimmung des Datentypes
var11 = "3"
print(var10 + int(var11)) #Umwandlung von Datentypen

#Python Operatoren #Python Operatoren 
#Python Operatoren #Python Operatoren 
#Python Operatoren #Python Operatoren 

a = 17
b = 0.3
c = 2
d = 0.65
print(1 * 1) #Multiplikation
print(1 + 1) #Addition
print(5 - 1) #Subtraktion
print(4 / 2) #Division
print(5 / 2) #Divison

print(a % c) #Modulo / Restwertberechnung
print(5//2) #Ganzzahldivision ohne Restwert
print(a ** c) #Potenz
print("a" + "b") #String Verkettung
print(a + 1.9)
print(False + True) #= 0 + 1 = 1
print(a + True) #=17 +1 = 18

myVar = 5
myVar *= 2 #myVar = myVar * 2 = 10
myVar %= 13
myVar **= 2

#Python Vergleichsoperatoren #Python Vergleichsoperatoren 
#Python Vergleichsoperatoren #Python Vergleichsoperatoren 
#Python Vergleichsoperatoren #Python Vergleichsoperatoren 

print(8 != 4 + 4) #ungleich
print(5 < 9) #kleiner
print(9 <= 9) # kleiner gleich
print(4 == 5) # ist gleich
print("4" == 4)
print(5 > 9) #größer als
print(5 >= 9) #größer gleich
print(4 >= 5)

#Python Logische Operatoren #Python Logische Operatoren 
#Python Logische Operatoren #Python Logische Operatoren 
#Python Logische Operatoren #Python Logische Operatoren 

print((4 + 4 == 8) and (2 + 3 == 5)) #Und Operator
print((4 +4 == 8) or (2 + 3 == 5)) #Oder Operator
print(not(1 + 4 == 5)) #Ergebnis wird umgedreht, also aus False wird True

#Python Weitere Operatoren #Python Weitere Operatoren 
#Python Weitere Operatoren #Python Weitere Operatoren 
#Python Weitere Operatoren #Python Weitere Operatoren 

pattern ="@"
seq1 = "Nick.Godau@ottobock.de"
print(pattern in seq1) #prüft ob Variable in Sequenz enthalten ist
print(pattern not in seq1) #prüft ob ein Pattern nicht in einer Sequenz enthalten ist
seq2 = "Nick.Godau@ottobock.de"
print("seq 1 is seq2", seq1 is seq2) #prüft ob seq1 auch seq2 ist
print("seq1 == seq2", seq1 == seq2) #prüft ob seq1 gleich seq2 ist
z1 = [2, 3, 5]
z2 = [2, 3, 5]
print("z1 is z2", z1 is z2)
print("z1 == z2", z1 == z2)

z1 = 2
a = z1 << 1 #Binärstelle wird nach Rechts verschoben
b = z1 >> 1 #Binärstelle wird nach Links verschoben
print("Der Wert von 2 << 1: ", a)
print("Der Wert von 2 >> 1: ", b)

#Kontrollstrukturen in Python #Kontrollstrukturen in Python
#Kontrollstrukturen in Python #Kontrollstrukturen in Python
#Kontrollstrukturen in Python #Kontrollstrukturen in Python

p = 3
if p < 2:
    print("Miese Zeiten")
    print("LOLOLLOLOLOL")

#IF-Else Anwweisung #IF-Else Anwweisung
#IF-Else Anwweisung #IF-Else Anwweisung
#IF-Else Anwweisung #IF-Else Anwweisung

#Bedinungen können in der Regel geklammert werden

up = 3
if up < 2:
    print("Miese Zeiten")
    print("JAOWOWWOOO")
elif up == 3:
    print("passt so Buder")
else:
    if(up == 4):
        print("Wert is 4")

#Python While Schleifen #Python While Schleifen
#Python While Schleifen #Python While Schleifen
#Python While Schleifen #Python While Schleifen

i = 0
while (i < 9): #Bedinung
    i += 1 #Schleife + 1
    print("Wert der Schleife ist :" + i)
print("Schleife zu Ende")

#For Schleife #For Schleife
#For Schleife #For Schleife
#For Schleife #For Schleife

zitat = "Werft den Purschen zu Poden"
zv = 0
for x in zitat:
    zv += 1
    print("Zeichen ", zv, ":\t", x)
print("Schleife beendet")

#Sprunganweisungen #Sprunganweisungen 
#Sprunganweisungen #Sprunganweisungen 
#Sprunganweisungen #Sprunganweisungen 

k = 0
while (True):
    k += 1
    print("Wert der Schleife", i)
    if k > 5:
        break #Beendet die Schleife
print("Schleife Beendet")


l = 0
while (l < 10):
    l += 1
    if (l % 2 != 0): continue #Beendet auch die Schleife wenn Variable nicht Modulo ist
    print ("Wert der Schleife ", l)
print("Schleife Beendet")

befehl = input("Geben sie einen Befehl ein : \nx\t: Ende\ns\tSpeichern\ns\tDrucken")
match befehl :
    case "x":
        print("Mensch was machen Sachen")
    case "s":
        print("Lass mal was cooles machen")
    case other:
        print("Kein Trefffer")

#Funktionen Deklarieren #Funktionen Deklarieren
#Funktionen Deklarieren #Funktionen Deklarieren
#Funktionen Deklarieren #Funktionen Deklarieren

def zitate():
    print("moin chef")
zitate() #Aufruf der funktion, egal wo einsetzbar

def multi(a,b):
    return a * b #Gibt den Wert zurück /Rückgabewert
    print("Test") #die Print Funktion wird wegen return nicht erreicht, unrecheable Code
print(multi(4,5))

az = 42
def ausgabe():
    global az #global greift auf vorher deklarierte Variable zu
    az += 1
    print(a)
ausgabe()
print(a)

