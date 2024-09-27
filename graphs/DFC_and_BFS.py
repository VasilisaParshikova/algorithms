# Поиск в глубину (DFS)
# Поиск в глубину (DFS) — это алгоритм обхода или поиска в графах, который начинает с корневого узла
# (или произвольного узла в графе) и исследует как можно дальше вдоль каждой ветви перед возвратом.
# Основной принцип DFS — погружение как можно глубже в граф, прежде чем переходить к соседним узлам.

# Поиск в ширину (BFS)
# Поиск в ширину (BFS) — это алгоритм обхода или поиска в графах, который начинает с корневого узла и
# исследует соседние узлы на текущем уровне перед переходом к узлам следующего уровня. Основной принцип BFS —
# исследование всех узлов на текущем уровне перед переходом на следующий уровень.

from collections import deque


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            stack.extend(reversed(graph[vertex]))


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            queue.extend(graph[vertex])


# Пример использования
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS:")
dfs(graph, 'A')  # Вывод: A B D E F C
print()
print("DFS (итеративный):")
dfs_iterative(graph, 'A')  # Вывод: A C F E B D
print()
print("BFS:")
bfs(graph, 'A')  # Вывод: A B C D E F
print()
