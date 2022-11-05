number = int(input('\n\tВведите число: '))

print('\tРезультат: ', end='')

if (number > 0) and (number < 10):
    for i in range(number):
        print(i + 1, end='')
else:
    print('Меньше одного или больше девяти')