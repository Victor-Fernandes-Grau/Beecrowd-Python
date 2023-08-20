x = int(input())
y = int(input())
soma = int(0)

if y % 2==0:
        y = y + 1
else:
        y = y+2
        
while x > y:
    soma = soma + y
    y = y+2
    
print(soma)
