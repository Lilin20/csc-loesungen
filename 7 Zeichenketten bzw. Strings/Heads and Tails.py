# Die Übung ist etwas komplizierter aber wenn du weißt wie du Strings zusammen fügst ist es doch relativ simpel.

tmp = input()
print(tmp[len(tmp) - 1] + tmp[1:len(tmp)-1] + tmp[0])