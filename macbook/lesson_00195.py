# Создаём список с дубликатами lst
lst = [0, 0, 1, 2, 3, 4, 5, 5, 6, 7]

# На основе списка создаём множество st
# Помним про основное свойство множеств - они не могут
# содержать дубликатов
# Поэтому если lst содержит дубликаты, то при создании
# множества на его основе дубликаты будут удалены
st = set(lst)

# А значит количество элементов в списке и во множестве
# будет различаться
# Сравниваем количество элементов с помощью встроенного
# метода len()
print(len(st) == len(lst))
