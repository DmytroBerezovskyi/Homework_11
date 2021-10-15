from random import randint
m = int(input('Введите кол-во колонок: '))
n = int(input('Введите кол-во строк: '))

lst = [[randint(1, 99) for _ in range(m)] for _ in range(n)]
print()

for i in lst:
    r = 0
    for j in i:
        r = r + j
        print(
                 '{v11:>5}'.format(v11=j), end=' ')
    print('   ', r)

print()
k = []
for g in range(m):
    r = 0
    for i in lst:
        r = i[g]+r

    k.append(r)
    print(
                 '{v12:>5}'.format(v12=r), end=' ')
