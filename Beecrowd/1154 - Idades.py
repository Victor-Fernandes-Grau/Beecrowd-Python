x = int(input())
cont = int(0)
cont2 = int(0)
resu = float(0.00)
while x >= 0:
    cont = cont + x
    cont2 = cont2 + 1
    x = int(input())

resu = cont / cont2
print(f'{resu:.2f}')
    
