# Стек (stack) — это структура данных, работающая по принципу LIFO (Last In, First Out),
# где последний добавленный элемент удаляется первым. Очередь (queue) — это структура данных, работающая по принципу
# FIFO (First In, First Out), где первый добавленный элемент удаляется первым. Основное различие между ними заключается
# в порядке удаления элементов: стек удаляет последний добавленный элемент, а очередь — первый.

# Реализации без библиотек, полностью свои

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Добавляет элемент в конец стека"""
        self.stack.append(item)

    def pop(self):
        """Удаляет и возвращает последний элемент из стека"""
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """Возвращает последний элемент стека без удаления"""
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        """Проверяет, пуст ли стек"""
        return len(self.stack) == 0

    def size(self):
        """Возвращает размер стека"""
        return len(self.stack)

# Пример использования
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Вывод: 3
print(stack.peek()) # Вывод: 2
print(stack.size()) # Вывод: 2

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Добавляет элемент в конец очереди"""
        self.queue.append(item)

    def dequeue(self):
        """Удаляет и возвращает первый элемент из очереди"""
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("dequeue from empty queue")

    def peek(self):
        """Возвращает первый элемент очереди без удаления"""
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("peek from empty queue")

    def is_empty(self):
        """Проверяет, пуста ли очередь"""
        return len(self.queue) == 0

    def size(self):
        """Возвращает размер очереди"""
        return len(self.queue)

# Пример использования
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Вывод: 1
print(queue.peek())     # Вывод: 2
print(queue.size())     # Вывод: 2


# реализация с использованием collections

from collections import deque

# Создание стека
stack = deque()

# Операции со стеком
stack.append(1)    # Добавление элемента в стек
stack.append(2)
stack.append(3)
print(stack.pop()) # Удаление и возврат последнего элемента: 3
print(stack[-1])   # Просмотр последнего элемента без удаления: 2
print(len(stack))  # Размер стека: 2
print(stack)       # Текущий стек: deque([1, 2])


# Создание очереди
queue = deque()

# Операции с очередью
queue.append(1)       # Добавление элемента в конец очереди
queue.append(2)
queue.append(3)
print(queue.popleft())# Удаление и возврат первого элемента: 1
print(queue[0])       # Просмотр первого элемента без удаления: 2
print(len(queue))     # Размер очереди: 2
print(queue)          # Текущая очередь: deque([2, 3])