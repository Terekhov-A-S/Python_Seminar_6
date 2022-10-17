# Программа для поиска совпадений между двумя списками, используя функцию filter


lst1 = ["Автомобиль", "Компрессор", "Дача", "Холодильник"]
lst2 = ["Автомобиль", "Учеба", "Самолет",
         "Холодильник", "Температура", "Компрессор"]


def filter_duplicate(string_to_check):
    if string_to_check in cnt:
        return False
    else:
        return True


cnt = lst2
out_filter = list(filter(filter_duplicate, lst1))
cnt = lst1
out_filter += list(filter(filter_duplicate, lst2))

print("Отфильтрованный список:", out_filter)
