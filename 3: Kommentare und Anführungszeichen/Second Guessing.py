# In dieser Aufgabe verbirgt sich ein Logikfehler und ein ungewolltest Kommentar.

# Ziel: gib die Zahl der Sekunden in einer Woche an
SekundenProMinute = 60
SekundenProStunde = SekundenProMinute * 60 	# Diese Zeile hatte den Logikfehler. Eine Minute hat nähmlich 60 Sekunden und nicht 50.
SekundenProTag = SekundenProStunde * 24
TageProWoche = 5
TageProWoche = TageProWoche + 2			# Diese Zeile war auskommentiert. Deshalb wurden in der Berechnung nur 5 Tage genommen anstatt 7.
print(SekundenProTag * TageProWoche)
