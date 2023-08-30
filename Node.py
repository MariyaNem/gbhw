from typing import Optional

# Класс, представляющий узел красно-черного дерева:
class Node:

    # Инициализация узла:
    def __init__(self, value: object, color: str) -> None:
        self.value = value
        self.color = color
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None