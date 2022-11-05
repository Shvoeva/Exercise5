number = int(input('\n\tВведите число: '))

print('\tРезультат: ', end='')

if number >= 0:
    if number % 2 == 1:
        print('Плохо')
    elif (number >= 2) and (number <= 5):
        print('Неплохо')
    elif (number >= 6) and (number <= 20):
        print('Так себе')
    else:
        print('Отлично')
else:
    print('Число отрицательное')