# In Variablen werden wie schon gelernt Werte gespeichert.
# Wir können immer und immer wieder neue Variablen erstellen mit oder ohne Werte.
# Diese Aufgabe kann man entweder mit mehreren Zeilen lösen oder direkt mit einer Zeile.

# Mehrere Zeilen.
tmp_x = x
x = y
y = tmp_x
# Hier verwendet man 3 Variablen um die Werte zu tauschen. In der tmp_x Variable wird der Wert für x zwischen gespeichert.
# tmp_* ist keine Sonderregelung. Die Variable heißt einfach nur so.
# Hierbei muss man den Wert von x oder y zwischenspeichern weil ansonsten das passiert:

x = 2 # Die 2 Zeilen hier dienen nur zur demonstration.
y = 4

x = y # x = 4
y = x # y = 4

# Hier ist nun also ein Fehler passiert. x und y haben den selben Wert und die beiden Werte wurden nicht getauscht.


# Eine Zeile
x, y = y, x

# Dies wird später erklärt.
