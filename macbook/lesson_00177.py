from heapq import nlargest
# найти три ключа с самыми высокими значениями в словаре

my_dict = {'a':500, 'b':5874, 'c':560, 'd':400, 'e':5874, 'f':20}

# функция sorted

ult = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(ult)

# аналогичный результат можно получить с помозью функции
# nlargest из модуля heapq

result = nlargest(3, my_dict, key=my_dict.get)
print(result)
