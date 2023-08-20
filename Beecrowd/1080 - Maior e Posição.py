contx = int(0)
maior = int(0)

while contx < 100:
    
    x = int(input())
    contx = contx +1

    if x > maior:
        maior = x
        con = int(contx)

print(maior)
print(con)

