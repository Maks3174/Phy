import  math
epsilon = float(input("Введіть точність: "))
sum = 0
x = 1
for x in range(1, 6):
    infinite_sum = 0
    k = 0
    while True:
        element = ((-1) ** (k + 1) * x ** (2*k + 1)) / (math.factorial(k) * (2*k + 1))
        infinite_sum += element
        if abs(element) < epsilon:
            break
        else:
            k += 1
    sum = infinite_sum
print(sum)

#2
parne_chislo = int(input("Введіть парне число: "))

if parne_chislo % 2 == 0:
    kilkist_neparnyh = parne_chislo // 2
    print(f"Кількість непарних чисел в парному числі {parne_chislo}: {kilkist_neparnyh}")
else:
    print("Введене число не є парним.")