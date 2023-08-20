a,b,c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)

r1 = (a*c)/2
r2 = 3.14159*(c*c)
r3 = ((a+b)*c)/2
r4 = b*b
r5 = a*b

print(f'TRIANGULO: {r1:.3f}')
print(f'CIRCULO: {r2:.3f}')
print(f'TRAPEZIO: {r3:.3f}')
print(f'QUADRADO: {r4:.3f}')
print(f'RETANGULO: {r5:.3f}')
