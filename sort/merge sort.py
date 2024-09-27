# На примере сортировки слиянием мы посмотрим на алгоритм типа «разделяй и властвуй» (divide and conquer).
# Алгоритмы этого типа работают, разделяя крупную задачу на более мелкие, решаемые проще.
# При сортировке слиянием мы разделяем массив пополам до тех пор, пока каждый участок не станет длиной в один элемент.
# Затем эти участки возвращаются на место (сливаются) в правильном порядке.
# Для работы алгоритма мы должны реализовать следующие операции:
# Операцию для рекурсивного разделения массива на группы (метод merge_sort).
# Слияние в правильном порядке (метод merge).

# Сложность  в среднем   лучший      худший
# Время      O(n*lod n)  O(n*lod n)  O(n*lod n)
# Пямять        O(n)     O(n)      O(n)

# Стоит отметить, что в отличие от линейных алгоритмов сортировки, сортировка слиянием будет делить и склеивать
# массив вне зависимости от того, был он отсортирован изначально или нет. Поэтому, несмотря на то, что в худшем случае
# он отработает быстрее, чем линейный, в лучшем случае его производительность будет ниже, чем у линейного.
# Поэтому сортировка слиянием — не самое лучшее решение, когда надо отсортировать частично упорядоченный массив.


from random import randint

N = 10  # количество элементов в списке
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)  # вывод исходного неотсортированного списка
iterations = 0
swaps = 0


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Т. к. длина списков применяется часто, создадим для удобства переменные
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если 1-й элемент левого подсписка меньше, добавляем его
            # в сортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если 1-й элемент правого подсписка меньше, добавляем его
            # в сортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Когда достигнут конец левого списка, добавляем элементы правого списка
        # в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Когда достигнут конец правого списка, добавляем элементы левого списка
        # в сортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
        global iterations
        iterations += 1
    print('сортировка', sorted_list)
    return sorted_list


def merge_sort(nums):
    # Возвращаем список, когда он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Чтобы найти середину списка, применяем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    print('разделение', nums[:mid], '\t', nums[mid:])

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем сортированные списки в результирующий
    return merge(left_list, right_list)


print(merge_sort(a))
print(iterations)

