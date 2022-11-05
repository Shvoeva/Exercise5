number = int(input('\n\tВведите число: '))

print('\tРезультат: ', end='')

if number >= 0:
    if number % 3 == 0 and number % 5 == 0:
        print('Fizz Buzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(str(number))
else:
    print('Число отрицательное')