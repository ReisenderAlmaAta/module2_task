v = int(input('Введите скорость: '))
t = int(input('Введите время: '))
mcad = 109
way = v * t
result  = way % mcad

print('Байкер Вася остановится возле отметки: ', result)