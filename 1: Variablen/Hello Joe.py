# Hier wift Zeile 2 einen Laufzeitfehler.

print("Hello")
username = Joe	# Joe wird hier als eine Variable interpretiert. Joe ist aber keine Variable weil diese nicht erstellt wurde.
print(username)

# Lösung
print("Hello")
username = "Joe"
print(username)
