n = int(input())

while n > 0:
    numero = int(input())
    QtdDiv=0
    for count in range(2,numero):
        if (numero % count == 0):
            QtdDiv += 1

    if(QtdDiv==0):
        print(numero,"eh primo")
    else:
        print(numero,"nao eh primo")
    n -=1
        
