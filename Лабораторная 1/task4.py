users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
total = len(users)
users = set(users)
unique = len(users)
logs = {
    "Общее количество": total,
    "Уникальные посещения": unique
}
print(logs)