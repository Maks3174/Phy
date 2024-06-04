size = int(input('Введіть розмір сторини квадрати (от 1 до 7): '))
mat = [[' '] * size for _ in range(size)]

n = input('Введіть букву від а до к\n')

i = 0
while i < size:
    k = 0
    while k < size:
        if (
            (n == 'а' and (i < k and i < size - 1 - k or i < k and i > size - 1 - k)) or
            (n == 'б' and (i > k and i < size - 1 - k or i > k and i > size - 1 - k)) or
            (n == 'в' and i < k and i < size - 1 - k) or
            (n == 'г' and i > k and i > size - 1 - k) or
            (n == 'д' and (i > k and i > size - 1 - k or i < k and i < size - 1 - k)) or
            (n == 'е' and (i > k and i < size - 1 - k or i < k and i > size - 1 - k)) or
            (n == 'ж' and i > k and i < size - 1 - k) or
            (n == 'з' and i < k and i > size - 1 - k) or
            (n == 'и' and (i < k and i < size - 1 - k or i > k and i < size - 1 - k)) or
            (n == 'к' and (i > k and i > size - 1 - k or i < k and i > size - 1 - k))
        ):
            mat[i][k] = '*'
        k += 1
    i += 1

for row in mat:
    print(*row)