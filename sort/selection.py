#Сортировка выбором — это некий гибрид между пузырьковой и сортировкой вставками.
# Как и сортировка пузырьком, этот алгоритм проходит по массиву раз за разом,
# перемещая одно значение на правильную позицию. Однако, в отличие от пузырьковой сортировки,
# он выбирает наименьшее неотсортированное значение вместо наибольшего. Как и при сортировке вставками,
# упорядоченная часть массива расположена в начале, в то время как в пузырьковой сортировке она находится в конце.
# Алгоритм
# Найти наименьшее значение в списке.
# Записать его в начало списка, а первый элемент - на место, где раньше стоял наименьший.
# Снова найти наименьший элемент в списке. При этом в поиске не участвует первый элемент.
# Второй минимум поместить на второе место списка. Второй элемент при этом перемещается на освободившееся место.
# Продолжать выполнять поиск и обмен, пока не будет достигнут конец списка.
# Сложность  в среднем   лучший    худший
# Время        O(n^2)    O(n)      O(n^2)
# Пямять        O(1)     O(1)      O(1)

from random import randint

N = 10  # количество элементов в списке
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)  # вывод исходного неотсортированного списка

# В цикле переменная i хранит индекс ячейки,
# в которую записывается минимальный элемент.
# Сначала это будет первая ячейка.
i = 0
iterations = 0
swaps = 0
# N - 1, так как последний элемент
# обменивать уже не надо.
while i < N - 1:

    # ПОИСК МИНИМУМА
    # Сначала надо найти минимальное значение
    # на срезе от i до конца списка.
    # Переменная m будет хранить индекс ячейки
    # с минимальным значением.
    # Сначала предполагаем, что
    # в ячейке i содержится минимальный элемент.
    m = i
    # Поиск начинаем с ячейки следующей за i.
    j = i + 1
    # Пока не дойдем до конца списка,
    while j < N:
        # будем сравнивать значение ячейки j,
        # со значением ячейки m.
        if a[j] < a[m]:
            # Если в j значение меньше, чем в m,
            # сохраним в m номер найденного
            # на данный момент минимума.
            m = j
        # Перейдем к следующей ячейке.
        j += 1
        iterations += 1

    # ОБМЕН ЗНАЧЕНИЙ
    # В ячейку i записывается найденный минимум,
    # а значение из ячейки i переносится
    # на старое место минимума.
    a[i], a[m] = a[m], a[i]
    swaps += 1
    print(a)

    # ПЕРЕХОД К СЛЕДУЮЩЕЙ НЕОБРАБОТАННОЙ ЯЧЕЙКЕ
    i += 1


# Вывод отсортированного списка
print(a)
print(iterations)
print(swaps)