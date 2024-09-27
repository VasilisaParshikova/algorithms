class TreeNode:
    """Класс узла дерева"""
    def __init__(self, key):
        self.key = key      # Ключ или значение узла
        self.left = None    # Левый потомок
        self.right = None   # Правый потомок

class BinaryTree:
    """Класс бинарного дерева"""
    def __init__(self):
        self.root = None    # Корень дерева

    def insert(self, key):
        """Вставка нового узла с заданным ключом в первое свободное место"""
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
        else:
            queue = [self.root]
            while queue:
                node = queue.pop(0)
                if node.left is None:
                    node.left = new_node
                    break
                else:
                    queue.append(node.left)
                if node.right is None:
                    node.right = new_node
                    break
                else:
                    queue.append(node.right)

    def search(self, key):
        """Поиск узла с заданным ключом"""
        if self.root is None:
            return None
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.key == key:
                return node
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return None

    def inorder(self):
        """Обход дерева в порядке Левый потомок, Корень, Правый потомок (inorder traversal)"""
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        """Рекурсивная функция inorder обхода"""
        if node:
            self._inorder(node.left)
            print(node.key, end=' ')
            self._inorder(node.right)

    def preorder(self):
        """Обход дерева в порядке прямого обхода Корень, Левый потомок, Правый потомок (preorder traversal)"""
        self._preorder(self.root)
        print()

    def _preorder(self, node):
        """Рекурсивная функция preorder обхода"""
        if node:
            print(node.key, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        """Обход дерева в порядке обратного обхода Левый потомок, Правый потомок, Корень. (postorder traversal)"""
        self._postorder(self.root)
        print()

    def _postorder(self, node):
        """Рекурсивная функция postorder обхода"""
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.key, end=' ')

# Пример использования
bt = BinaryTree()
bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)

print("Inorder traversal:")
bt.inorder()  # Вывод: 4 2 5 1 3

print("Preorder traversal:")
bt.preorder() # Вывод: 1 2 4 5 3

print("Postorder traversal:")
bt.postorder()# Вывод: 4 5 2 3 1

print("Поиск 4:", bt.search(4) is not None)  # Вывод: Поиск 4: True
print("Поиск 6:", bt.search(6) is not None)  # Вывод: Поиск 6: False
