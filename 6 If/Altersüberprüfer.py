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
