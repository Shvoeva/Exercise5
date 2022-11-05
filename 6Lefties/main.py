text = ["bright aright", "ok"]
counter = 0

for i in text:
    text[counter] = i.replace('right', 'left')
    counter += 1

result = ','.join(text)

print(f'\n\tРезультат: {result}')