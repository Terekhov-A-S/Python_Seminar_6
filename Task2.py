# Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.

def tesaurus(*names):
    res = {}
    for name in names:
        key = name[0].capitalize()
        if key not in res:
            res[key] = []
        res[key].append(name)
    return res


print(tesaurus("Егор", "Вячеслав", "Виктор", "Ира", "Наталья", "Афанасий"))
