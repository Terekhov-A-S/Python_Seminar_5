# ****** Код для удаления "абв" из введенного пользователем набора букв******

print('Удаляем из текста набор букв: "абв"')
set_word = input('Введите текс (на русском языке) : ').split()

set_word2 = ' '.join([set_word[i] for i in range(len(set_word)) if 'абв' not in set_word[i]])
print(set_word2)




# ****** Код для удаления рандомно сформированных наборов букв, состоящих из "абв" ******
# import random
#
# number_of_words = (int(input("Задайте желаемое количество слов в тексте: ")))
# set_word1 = []
#
# set_of_letters = "абв"
# print(f'Удаляем из текста набор букв: "{set_of_letters}"')
#
# print('Вновь сформированный набор слов: ')
# for i in range(number_of_words):
#     random_letters = random.sample(set_of_letters, 3)
#     set_word1.append("".join(random_letters))
#
# print(" ".join(set_word1))
#
# print(f'Набор слов с исключенным "{set_of_letters}": ')
# set_word2 = list(filter(lambda i: set_of_letters not in i, set_word1))
# print(" ".join(set_word2))
