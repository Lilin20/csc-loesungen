n = int(input())

for i in range(1 , (n + 1)):
    for j in range(1, (n+1)):
        if i * j == n:
            print(str(i)+" times "+str(j)+" equals "+str(n))