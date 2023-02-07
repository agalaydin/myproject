# Выведите вск элементы меньше 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for n in a:
    if n < 5:
        print(n)


# Также можно воспользоваться функцией filter, которая фильтрует элементы
# согласно заданному условию:

print(list(filter(lambda elem: elem < 5, a)))

# наиболее предпочтительный вариант решения этой задачи,
# списковое включение

print([elem for elem in a if elem < 5])