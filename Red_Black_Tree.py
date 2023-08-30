from typing import Optional, Union
from Node import Node


# Класс для красно-черного дерева:
class RBTree:

    # Инициализируем дерево:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    # Делаем проверку добавляемых в дерево данных:
    def _check_type(self, value):
        return type(self.root.value) == type(value)

    def insert(self, value: object) -> None:
        # Создаем новый узел красного цвета:
        new_node = Node(value, "красный")

        # Если дерево пустое, создаваемый узел становится корнем и приобретает "черный" цвет:
        if self.root is None:
            self.root = new_node
            self.root.color = "черный"

        # Иначе, вызываем поверку на соответствие типов:
        elif self._check_type(value):
            self._insert_node(self.root, new_node)
        else:
            print(f"Это дерево может работать только с {type(self.root.value)}")

    # Вспомогательная функция для вставки узла в дерево:
    def _insert_node(self, current: Node, new_node: Node) -> None:
        # Если значение нового узла меньше значения текущего узла, переходим к левому поддереву:
        if new_node.value < current.value:
            if current.left is None:
                # Если левого поддерева нет, новый узел становится левым потомком текущего узла:
                current.left = new_node
                new_node.parent = current
            else:
                # Иначе, вызываем функцию для левого поддерева:
                self._insert_node(current.left, new_node)
        else:
            if current.right is None:
                # Если правого поддерева нет, новый узел становится правым потомком текущего узла:
                current.right = new_node
                new_node.parent = current
            else:
                # Иначе, вызываем функцию для правого поддерева:
                self._insert_node(current.right, new_node)

        # Вызываем функцию для восстановления свойств красно-черного дерева:
        self._fix_insertion(new_node)

    # Функция восстановления свойств красно-черного дерева после вставки узла:
    def _fix_insertion(self, node: Node) -> None:
        while node.parent is not None and node.parent.color == "красный":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                # Случай 1: Дядя узла является красным:
                if uncle is not None and uncle.color == "красный":
                    node.parent.color = "черный"
                    uncle.color = "черный"
                    node.parent.parent.color = "красный"
                    node = node.parent.parent
                else:
                    # Случай 2: Узел является правым потомком своего родителя:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    # Случай 3: Узел является левым потомком своего родителя:
                    node.parent.color = "черный"
                    node.parent.parent.color = "красный"
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                # Случай 1: Дядя узла является красным:
                if uncle is not None and uncle.color == "красный":
                    node.parent.color = "черный"
                    uncle.color = "черный"
                    node.parent.parent.color = "красный"
                    node = node.parent.parent
                else:
                    # Случай 2: Узел является левым потомком своего родителя:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    # Случай 3: Узел является правым потомком своего родителя:
                    node.parent.color = "черный"
                    node.parent.parent.color = "красный"
                    self._rotate_left(node.parent.parent)

        # Корень всегда окрашивается в "черный" цвет:
        self.root.color = "черный"

    # Левый поворот поддерева относительно заданного узла:
    def _rotate_left(self, node: Node) -> None:
        new_node = node.right
        node.right = new_node.left
        if new_node.left is not None:
            new_node.left.parent = node
        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node
        new_node.left = node
        node.parent = new_node

    # Правый поворот поддерева относительно заданного узла:
    def _rotate_right(self, node: Node) -> None:
        new_node = node.left
        node.left = new_node.right
        if new_node.right is not None:
            new_node.right.parent = node
        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.right:
            node.parent.right = new_node
        else:
            node.parent.left = new_node
        new_node.right = node
        node.parent = new_node

    # Поиск узла с заданным значением в дереве:
    def search(self, value: object) -> Union[object, None]:
        res = self._find_node(self.root, value)
        return res if res is None else res.value

    # Удаление значения из дерева:
    def delete(self, value: object) -> None:
        # Находим узел с заданным значением:
        if self._check_type(value):
            node_to_delete = self._find_node(self.root, value)
            if node_to_delete is None:
                return

            # Вызываем вспомогательную функцию для удаления узла:
            self._delete_helper(node_to_delete)

    # Вспомогательная функция для поиска узла с заданным значением:
    def _find_node(self, current: Node, value: object) -> Optional[Node]:
        if current is None or current.value == value:
            return current
        if value < current.value:
            return self._find_node(current.left, value)
        return self._find_node(current.right, value)

    # Вспомогательная функция для удаления узла из дерева:
    def _delete_helper(self, node: Node) -> None:
        # Находим узел, который будет удален из дерева:
        if node.left is not None and node.right is not None:
            successor = self._minimum(node.right)
            node.value = successor.value
            node = successor

        # Определяем потомка узла, который будет удален:
        child = node.left if node.left is not None else node.right

        # Удаляем узел из дерева:
        if node.color == "черный" and child is Node:
            node.color = child.color
            self._delete_case1(node)
        self._swap_node(node, child)

    @staticmethod
    # Нахождение узла с минимальным значением в поддереве:
    def _minimum(node: Node) -> Node:
        while node.left is not None:
            node = node.left
        return node

    # Правило 1 для удаления узла из дерева:
    def _delete_case1(self, node: Node) -> None:
        if node.parent is None:
            return
        self._delete_case2(node)

    # Правило 2 для удаления узла из дерева:
    def _delete_case2(self, node: Node) -> None:
        sibling = self._sibling(node)
        if sibling.color == "красный":
            node.parent.color = "красный"
            sibling.color = "черный"
            if node == node.parent.left:
                self._rotate_left(node.parent)
            else:
                self._rotate_right(node.parent)
        self._delete_case3(node)

    # Правило 3 для удаления узла из дерева:
    def _delete_case3(self, node: Node) -> None:
        sibling = self._sibling(node)
        if (node.parent.color == "черный" and sibling.color == "черный" and
                sibling.left.color == "черный" and sibling.right.color == "черный"):
            sibling.color = "красный"
            self._delete_case1(node.parent)
        else:
            self._delete_case4(node)

    # Правило 3 для удаления узла из дерева.
    def _delete_case4(self, node: Node) -> None:
        sibling = self._sibling(node)
        if sibling is not None and (node.parent.color == "красный" and sibling.color == "черный" and
                                    sibling.left is not None and sibling.left.color == "черный" and
                                    sibling.right is not None and sibling.right.color == "черный"):
            sibling.color = "красный"
            node.parent.color = "черный"
        else:
            self._delete_case5(node)

    # Правило 5 для удаления узла из дерева:
    def _delete_case5(self, node: Node) -> None:
        # Обработка случая, когда узел node является корневым узлом:
        if node.parent is None:
            return

        sibling = self._sibling(node)
        # Обработка случая, когда узел node не имеет sibling:
        if sibling is None:
            return

        if sibling.color == "черный":
            if (node == node.parent.left and
                    (sibling.right is None or sibling.right.color == "черный") and
                    sibling.left.color == "красный"):
                sibling.color = "красный"
                sibling.left.color = "черный"
                self._rotate_right(sibling)
            elif (node == node.parent.right and sibling.left.color == "черный" and
                  sibling.right.color == "красный"):
                sibling.color = "красный"
                sibling.right.color = "черный"
                self._rotate_left(sibling)
        self._delete_case6(node)

    # Правило 6 для удаления узла из дерева:
    def _delete_case6(self, node: Node) -> None:
        sibling = self._sibling(node)
        sibling.color = node.parent.color
        node.parent.color = "черный"
        if node == node.parent.left:
            sibling.right.color = "черный"
            self._rotate_left(node.parent)
        else:
            sibling.left.color = "черный"
            self._rotate_right(node.parent)

    @staticmethod
    # Возвращает брата узла:
    def _sibling(node: Node) -> Node:
        if node == node.parent.left:
            return node.parent.right
        return node.parent.left

    # Замена узла в дереве:
    def _swap_node(self, node: Node, child: Node) -> None:
        if child is not None:
            child.parent = node.parent
        if node.parent is None:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child

    # Преобразование дерева в список:
    def to_list(self) -> list:
        result = []
        self._traverse_inorder(self.root, result)
        return result

    # Вспомогательная функция для обхода дерева в порядке "inorder" (левое поддерево, узел, правое поддерево):
    def _traverse_inorder(self, node: Node, result: list) -> None:
        if node is not None:
            self._traverse_inorder(node.left, result)
            result.append(node.value)
            self._traverse_inorder(node.right, result)

    # Вывод дерева в терминал:
    def print_tree(self) -> None:
        self._print_tree_helper(self.root, "", True)

    # Вспомогательная функция для вывода дерева в терминал:
    def _print_tree_helper(self, node: Node, indent: str, last: bool) -> None:
        if node is not None:
            print(indent, end="")
            if last:
                print("\\-- ", end="")
                indent += "   "
            else:
                print("|-- ", end="")
                indent += "|  "

            print(f"{node.value} ({node.color})")

            self._print_tree_helper(node.left, indent, False)
            self._print_tree_helper(node.right, indent, True)