# Bei dieser Aufgabe ist es wichtig NICHT mit Boolean-Operatoren zu arbeiten (Erklärung kommt später).
# Ebenso sollen hier keine weiteren Boolean-Überprüfungen verwendet werden.
# Diese beiden Sachen erleichtern diese Aufgabe zwar enorm aber hier wird getestet ob man das verschachteln sinvoll nutzen kann.

age = int(input())

if age >= 0:
 if age < 18:
  print("Too young to vote")

if age < 0:
 print("You are a time traveller")

if age >= 18:
 print("You can vote")


# Lösung mit Boolean-Operatoren und Boolean-Überprüfungen

if age >= 0 and age < 18:
 print("Too young to vote")

elif age < 0:
 print("You are a time traveller")

else:
 print("You can vote")
