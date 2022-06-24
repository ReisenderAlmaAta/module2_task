num1 = float(input('Введите число 1: '))
num2 = float(input('Введите число 2: '))

max1 = (num1 > num2) * num1 + (num2 >= num1) * num2

print(max1)