# Hier musst du angeben WELCHE Ausgabe nicht möglich ist.
# Dafür guckt man sich am besten NUR die erste IF-Abfrage an.

if password=='openSesame':
  print('User logged on.')
  if hour>17:
    print('Good evening!')
  print('Enter a command:')

# Die erste IF-Abfrage (if password...) beinhaltet 2 Prints. Diese werden IMMER ausgegeben.
# Das Print in der zweiten IF-Abfrage ist egal ob es ausgeführt wird. Das können wir ignorieren.
# Es ist demnach nicht möglich das es NUR eine Ausgabe gibt. Es gibt minimal keine Ausgabe.
