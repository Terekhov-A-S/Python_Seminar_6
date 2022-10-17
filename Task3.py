# Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.


result_spisok = []
spisok = [int(i) for i in input("Введите набор чисел через пробел: ").split()]
for i in range(1, len(spisok)):
    if spisok[i] > spisok[i - 1]:
        (result_spisok.append(spisok[i]))
print("Исходный список: ", spisok)
print("Список элементов, значения которых больше предыдущих элементов: ", result_spisok)
