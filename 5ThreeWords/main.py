text = input('\n\tВведите текст: ')
text.strip(' ')

list_word = text.split()
answer = False
counter = 0

for i in list_word:
    if i.isdigit():
        counter = 0
    else:
        counter += 1

        if counter == 3:
            answer = True
            break

print(f'\tРезультат: {answer}')