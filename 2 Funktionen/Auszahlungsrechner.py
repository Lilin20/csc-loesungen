# Bedenke: Guck dir genau die MIN und MAX Funktionen an.
# Wir fangen am besten bei der hinteren an.
# max(balance*0.021, 10) - Hier gucken wir ob die 2,1% unseres Geldes mehr sind als 10
# min(balance, max(balance*0.021, 10)) - Nun wird geguckt welcher der kleine Betrag ist, da wir ja wissen müssen ob der Minimalbetrag unseren Balance sprengen würde.

print(min(balance, max(balance*0.021, 10)))
