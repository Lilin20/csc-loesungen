a, b = int(input()), int(input())

tmp = a % b

divisible = "divisible" if tmp <= 0 else "not divisible"
print(divisible)