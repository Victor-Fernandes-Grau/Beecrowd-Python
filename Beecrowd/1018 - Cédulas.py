x = int(input())
sobra = x

n100 = sobra//100
sobra = sobra - (n100*100)

n50 = sobra//50
sobra = sobra - (n50*50)

n20 = sobra//20
sobra = sobra - (n20*20)

n10 = sobra//10
sobra = sobra - (n10*10)

n5 = sobra//5
sobra = sobra - (n5*5)

n2 = sobra//2
sobra = sobra - (n2*2)

n1 = sobra//1
sobra = sobra - (n1*1)

print(x)
print(n100, 'nota(s) de R$ 100,00')
print(n50, 'nota(s) de R$ 50,00')
print(n20, 'nota(s) de R$ 20,00')
print(n10, 'nota(s) de R$ 10,00')
print(n5, 'nota(s) de R$ 5,00')
print(n2, 'nota(s) de R$ 2,00')
print(n1, 'nota(s) de R$ 1,00')

