# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.


expedition_items = {
    'спальник': 3,
    'палатка': 6,
    'термос': 2,
    'топор': 2,
    'нож': 1,
    'консервы': 4,
    'лодка': 7,
    'фонарь': 2
}

approved_items = {}
backpack_weight = 10

sorted_items = sorted(expedition_items.items(), key=lambda x: x[1])

for item, value in sorted_items:
    if value <= backpack_weight:
        approved_items[item] = value
        backpack_weight -= value

print(approved_items)

