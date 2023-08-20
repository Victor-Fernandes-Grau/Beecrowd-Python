QtdCasos = int(input())
pontoJoao = int(0)
pontoMaria = int(0)
x = int(3)
y = int(3)
while QtdCasos > 0:
    while x > 0:
        joao, DistanJoao = input().split()
        joao = int(joao)
        DistanJoao = int(DistanJoao)
        pontoJoao = pontoJoao + (joao*DistanJoao)
        x -=1

    while y > 0:
        maria, Distanmaria = input().split()
        maria = int(maria)
        Distanmaria = int(Distanmaria)
        pontoMaria = pontoMaria + (maria*Distanmaria)
        y-=1
        
    if pontoJoao > pontoMaria:
        print('JOAO')
    else:
        print('MARIA')
    pontoJoao = 0
    pontoMaria = 0
    x = 3
    y = 3
    QtdCasos -= 1
