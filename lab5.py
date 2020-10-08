arr = []


def funadd(arr, x):
    i = 0
    while i <= x:
        y = input('vvedite naimenovanie tovara')
        arr.append(y)
        i = i + 1


def funprint(arr):
    x = ""
    for y in arr:
        x += "\n" + y
    return x


def funudal(arr, x):
        arr.pop(x)


print('0)vivod spiska')
print('1)dobavlenie tovara v spisok')
print('2)udalenie')
print('3)vihod')
i = 0
x = 3
while i <= x:
    d = int(input('input ur choise'))
    if d == 0:
        print(funprint(arr))
    elif d == 1:
        funadd(arr, 3)
    elif d == 2:
        k=int(input('vvedite index tovara dl9 udaleni9'))
        funudal(arr, k)
    elif d == 3:
        i = 4
