from task_four.tree import RBTree


def main():
    tree = RBTree()
    val_lst = [10, 5, 7, 16, 13, 2, 20, 3]
    for x in val_lst:
        tree.insert(x)
    print(tree)


main()
