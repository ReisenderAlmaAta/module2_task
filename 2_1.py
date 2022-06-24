a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))

if a == b and a == c:
	print(3)
elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
	print(2)
else:
	print(0)