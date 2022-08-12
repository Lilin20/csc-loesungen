# Um diese Übung zu lösen musst du die Paare in folgender Reihenfolge sortieren.
# (x, y) -> (y, z) -> (x, y)

tmp = max(x, y)
x = min(x, y)
y = tmp
tmp = max(y, z)
y = min(y, z)
z = tmp
tmp = max(x, y)
x = min(x, y)
y = tmp
