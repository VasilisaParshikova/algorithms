# Двоичное дерево поиска строится по определенным правилам:
#
# У каждого узла не более двух детей.
# Любое значение меньше значения узла становится левым ребенком или ребенком левого ребенка.
# Любое значение больше или равное значению узла становится правым ребенком или ребенком правого ребенка.

class TreeNode:
    """Класс узла дерева"""

    def __init__(self, key):
        self.key = key  # Ключ или значение узла
        self.left = None  # Левый потомок
        self.right = None  # Правый потомок


class BinarySearchTree:
    """Класс бинарного дерева поиска"""

    def __init__(self):
        self.root = None  # Корень дерева

    def insert(self, key):
        """Вставка нового узла с заданным ключом"""
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        """Рекурсивная функция вставки"""
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        """Поиск узла с заданным ключом"""
        return self._search(self.root, key)

    def _search(self, node, key):
        """Рекурсивная функция поиска"""
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        """Удаление узла с заданным ключом"""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """Рекурсивная функция удаления"""
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Узел с одним потомком или без потомков
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Узел с двумя потомками: получаем inorder-преемника (наименьший в правом поддереве)
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        return node

    def _min_value_node(self, node):
        """Получение узла с минимальным значением"""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        """Обход дерева в порядке возрастания (inorder traversal)"""
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        """Рекурсивная функция inorder обхода"""
        if node:
            self._inorder(node.left)
            print(node.key, end=' ')
            self._inorder(node.right)


# Пример использования
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder traversal после вставки:")
bst.inorder()  # Вывод: 20 30 40 50 60 70 80

print("Поиск 40:", bst.search(40) is not None)  # Вывод: Поиск 40: True
print("Поиск 90:", bst.search(90) is not None)  # Вывод: Поиск 90: False

bst.delete(20)
print("Inorder traversal после удаления 20:")
bst.inorder()  # Вывод: 30 40 50 60 70 80

bst.delete(30)
print("Inorder traversal после удаления 30:")
bst.inorder()  # Вывод: 40 50 60 70 80

bst.delete(50)
print("Inorder traversal после удаления 50:")
bst.inorder()  # Вывод: 40 60 70 80
