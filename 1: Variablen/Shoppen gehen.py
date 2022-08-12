# Der untenstehende Print bekommt einen falschen Wert übermittelt welcher das Ergebnis verfälscht.
# Der letzte Wert war "meatPrice" und wurde mit "milkPrice" ersetzt.

meatPrice = 4.00
meatTax = 0.03 * meatPrice
milkPrice = 2.00
milkTax = 0.03 * milkPrice
print(meatTax + meatPrice + milkTax + milkPrice)
