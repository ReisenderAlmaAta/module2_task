
while True: 

	count = 0
	count_len = 0
	count_upper = 0
	count_lower = 0

	print('Введите пароль')
	password = input()

	if len(password) >= 8:
		count_len += 1
	for letter in password:
		if letter.isupper():
			count_upper += 1
		else:
			count_lower += 1
	count = count_len * count_lower * count_upper
	
	if count < 3:
		print('Пароль не соответствует требованиям')
	else:
		print('Пароль принят')
		break
print('Ваш пароль: ', password)

