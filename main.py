from Red_Black_Tree import RBTree


def go():

    tree_str = RBTree()
    tree_str.insert("one")
    tree_str.insert("two")
    tree_str.insert("book")
    tree_str.insert("four")
    tree_str.insert("lake")
    tree_str.insert("street")
    tree_str.insert("seven")
    tree_str.insert("911")
    tree_str.insert(True)

    tree_str.print_tree()
    print()
    tree_digit = RBTree()

    tree_digit.insert(10)
    tree_digit.insert(20)
    tree_digit.insert(40)
    tree_digit.insert(60)
    tree_digit.insert(50.5)
    tree_digit.insert(80)
    tree_digit.insert(60)
    tree_digit.insert("100")
    tree_digit.insert(45)
    tree_digit.insert(90)
    tree_digit.insert(100)
    tree_digit.insert(45)
    tree_digit.insert(90)
    tree_digit.insert(25)
    tree_digit.print_tree()
    print()
    print(tree_digit.to_list(), tree_str.to_list(), sep="\n")
    print(">>> ", tree_str.search("python"))
    print(">>> ", tree_str.search("Python"))
    print(">>> ", tree_digit.search(40))
    tree_digit.delete(20)

    tree_digit.print_tree()


if __name__ == '__main__':
    go()