# Die vorgegebene Variable "inputStr" hat den Typen "String".
# Diese Variable beinhaltet aber nur Zahlen. Um genauer zu sein: Zahlen mit Dezimalstellen.
# Zuerst konvertieren wir den String in einen Float.

inputStr = float(inputStr)

# Dann berechnen wir den Flächeninhalt der Pizza.

A = inputStr * inputStr

# Jetzt nehmen wir nur noch den Flächeninhalt / 100 und konvertieren das Ergebnis in den Typen "Integer".

print(int(A / 100))
