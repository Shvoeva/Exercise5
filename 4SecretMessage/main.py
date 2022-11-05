text = input('\n\tВведите текст: ')

print('\tРезультат: ', end='')

for i in text:
    if i.isupper():
        print(i, end='')