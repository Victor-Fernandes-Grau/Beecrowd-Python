a,b,c,d = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
d = float(d)

media = ((a * 2) + (b * 3) + (c * 4) + (d * 1))/ 10

if media >= 7:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
elif media < 5:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
elif media >= 5 and media <= 6.9:
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    
    exa = float(input())
    print(f'Nota do exame: {exa:.1f}')

    MediaNova = (media + exa )/2
    if MediaNova >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    
    print(f'Media final: {MediaNova:.1f}')
