# Создайте список [18, 14, 10, 6, 2]

lst = []

# Пробегаемся циклом for по последовательности, которую формирует
# функция range()
# Начало диапозона: 18
# Конец диапозона: 1(обратите внимание, что 1 не включается в итоговую
# последовательность)
# Шаг: -4(обратный шаг - двигаемся в сторону уменьшения значений)
for item in range(18, 1, -4):
    lst.append(item)

print(lst)
