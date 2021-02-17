import random

words_bank = ['автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека',
              'шайба', 'олимпиада', 'снег', 'лед']
# random idx
#secret_word = random.choice(words_bank)
secret_word = random.choice(words_bank)
#print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(gamer_word)

#gamer_word[2] = 'б' # str - inmutable -> mutable -> list, not set
#print(gamer_word)
#print(''.join(gamer_word))

errors_cnt = 0
while True:
    letter = input('введите ОДНУ русскую букву:').lower()
    # letter validation: ord(), re
    if len(letter) != 1:
        continue
    print('Вы ввели:', letter)

    if letter in secret_word:
        idx = 0
        for idx, symbol in enumerate(secret_word): # (idx, item)
            if symbol == letter:
                gamer_word[idx] = letter
        if '*' not in gamer_word:
            print('Вы выиграли')
            print('было загадано слово:', secret_word.upper())
            break
    else:
        errors_cnt += 1
        print('ошибок допущено:' , errors_cnt)
        if errors_cnt == 8:
            print('YOU LOST')
            break
    print(''.join(gamer_word))

print('СПАСИБО ЗА ИГРУ!')
