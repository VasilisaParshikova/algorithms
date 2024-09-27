# Кодирование Хаффмена – это основа современного сжатия текстов.
# Суть его заключается в анализе частотности появления символов в тексте
# и построения на его основе дерева из этих символов.

# Шаги алгоритма Кодирования Хаффмана
# Подсчет частоты символов: Сначала определяется частота каждого символа в сообщении или тексте, который нужно сжать.
#
# Построение дерева Хаффмана: Создается двоичное дерево, где каждый лист соответствует символу с его частотой,
# а внутренние узлы — сумме частот двух дочерних узлов. Для построения используется минимальная куча (min-heap)
# или приоритетная очередь, чтобы всегда извлекать два узла с наименьшими частотами.
#
# Генерация кодов: Обход дерева от корня к каждому листу, генерируя коды Хаффмана.
# Левому потомку присваивается бит '0', а правому — '1'.
#
# Создание закодированного сообщения: Замена каждого символа в исходном сообщении его кодом Хаффмана.

import heapq   # Модуль для работы с минимальной кучей
from collections import defaultdict, Counter

class TreeNode:
    """Класс узла дерева Хаффмана"""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_map):
    """Строит дерево Хаффмана на основе карты частот"""
    priority_queue = [TreeNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)

        # Создаем новый узел, суммируя частоты левого и правого узлов
        new_node = TreeNode(None, left_node.freq + right_node.freq)
        new_node.left = left_node
        new_node.right = right_node

        # Добавляем новый узел обратно в приоритетную очередь
        heapq.heappush(priority_queue, new_node)

    # Возвращаем корень дерева Хаффмана
    return priority_queue[0]

def generate_huffman_codes(root, current_code, huffman_codes):
    """Генерирует коды Хаффмана для каждого символа"""
    if root is None:
        return

    # Если узел является листом (символ), добавляем его код в словарь кодов
    if root.char is not None:
        huffman_codes[root.char] = current_code
        return

    # Рекурсивно строим коды для левого и правого поддеревьев
    generate_huffman_codes(root.left, current_code + '0', huffman_codes)
    generate_huffman_codes(root.right, current_code + '1', huffman_codes)

def huffman_encoding(data):
    """Кодирует сообщение с использованием Хаффмана"""
    if len(data) == 0:
        return "", None

    # Подсчитываем частоту каждого символа в сообщении
    freq_map = Counter(data)

    # Строим дерево Хаффмана на основе карты частот
    root = build_huffman_tree(freq_map)

    # Генерируем коды Хаффмана для каждого символа
    huffman_codes = {}
    generate_huffman_codes(root, "", huffman_codes)

    # Кодируем исходное сообщение
    encoded_message = ''.join(huffman_codes[char] for char in data)

    return encoded_message, root

def huffman_decoding(encoded_message, root):
    """Декодирует закодированное сообщение с использованием Хаффмана"""
    if len(encoded_message) == 0:
        return ""

    decoded_message = []
    current_node = root

    for bit in encoded_message:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        # Если достигнут лист дерева, добавляем символ в раскодированное сообщение
        if current_node.char is not None:
            decoded_message.append(current_node.char)
            current_node = root  # Возвращаемся к корню для следующего символа

    return ''.join(decoded_message)

# Пример использования
if __name__ == "__main__":
    message = "abracadabra"

    encoded_message, tree_root = huffman_encoding(message)
    print("Закодированное сообщение:", encoded_message)  # Вывод: Закодированное сообщение: 001011101011001010011001011111101011

    decoded_message = huffman_decoding(encoded_message, tree_root)
    print("Раскодированное сообщение:", decoded_message)  # Вывод: Раскодированное сообщение: abracadabra
