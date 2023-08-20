x = int(input())

ano = x//365
x = x - (ano*365)

mes = x//30
x = x - (mes*30)

dia = x//1
x = x - (dia*1)
print(ano, 'ano(s)')
print(mes, 'mes(es)')
print(dia, 'dia(s)')
