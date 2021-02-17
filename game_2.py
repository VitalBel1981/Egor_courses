import random

words_bank = ['автострада', 'бензин', 'инопланетянин',
              'самолет', 'библиотека', 'шайба',
              'олимпиада', 'зима', 'снег', 'лед']

secret_word = random.choice(words_bank)
print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

# gamer_word[2] = 'у'
# print(''.join(gamer_word))
while True:
    letter = input('введите ОДНУ русскую букву: ').lower()
    # letter validation: ord(), re
    if len(letter) != 1:  # ==, !=
        continue

    print('вы ввели:', letter)
