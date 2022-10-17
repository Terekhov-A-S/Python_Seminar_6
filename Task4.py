# Пример использования нумерования (enumerate).

lst = [5, 3, 1, 0, 9, 7]
lst_num = list(enumerate(lst, 0))
t_max = max(lst_num, key=lambda i: i[1])
print(f'Индекс максимума: {t_max[0]}, Max число {t_max[1]}')
t_min = min(lst_num, key=lambda i: i[1])
print(f'Индекс минимума: {t_min[0]}, Min число {t_min[1]}')
