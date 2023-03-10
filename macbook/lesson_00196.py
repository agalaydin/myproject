# Создаём словарь
dct = {1: 'value_1', 2: 'value_2', 3: 'value_3'}
print(dct)

# Добавляем в словарь новый элемент с ключом 'str_key' и значением 12345
dct['str_key'] = 12345
print(dct)

# Добавляем в словарь новый элемент с ключом ('it', 'is', 'tuple')
# и значением [11, 22, 'list_value', 33, {1, 2, 3}]
dct[('it', 'is', 'tuple')] = [11, 22, 'list_value', 33, {1, 2, 3}]
print(dct)

# Получаем элемент словаря по ключу 'str_key'
# Способ 1: Напрямую - в случаем отсутствия ключа формируется исключение
item_by_key_v1 = dct['str_key']
print(item_by_key_v1)

# Способ 2: Через функцию get() - в случае отсутствия ключа возвращает
# дефолтное значение 'No item'
item_by_key_v2 = dct.get('str_key', 'No item')
print(item_by_key_v2)

# Удаляем элемент с ключом '2' из словаря
item_deleted = dct.pop(2, 'No item')
print(item_deleted)

# Получаем ключи словаря
# Возвращаемое значение: 
# dict_keys([1, 3, 'str_key', ('it', 'is', 'tuple')])
keys = dct.keys()
print(keys)

