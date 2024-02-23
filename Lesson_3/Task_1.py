# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

from random import randint

list_data = [randint(1, 10) for _ in range(20)]
print(list_data)

list_res = []
for item in list_data:
    if list_data.count(item) > 1 and item not in list_res:
        list_res.append(item)

print(list_res)
