# Für diese Sortierübung ist es nötig zu wissen WANN und WO eine Variable definiert wird.
# Hier musst du genau gucken welcher Wert in welcher Variable gespeichert wird.
# z.B. kannst du "averageSpeed" NICHT an erster Stelle setzen.
# "averageSpeed" hängt von 2 Variablen ab. Diese 2 Variablen werden mithifle von bereits vorhandenen Variablen berechnet.
# Ein Python-Programm verläuft von OBEN nach UNTEN.

totalDistance = uphillDistance + downhillDistance # Variable totalDistance bekommt einen Wert.
totalTime = uphillTime + downhillTime		  # Variable totalTime bekommt einen Wert.
averageSpeed = totalDistance / totalTime	  # Die 2 Variablen können nun genutzt werden um averageSpeed zu setzen.
print(averageSpeed)
