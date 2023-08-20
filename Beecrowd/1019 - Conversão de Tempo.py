x = int(input())

h = x // 3600
x = x - (h*3600)

m = x // 60
x = x - (m*60)

s = x // 1
x = x - (h*1)

print(f'{h:}:{m:}:{s:}')
