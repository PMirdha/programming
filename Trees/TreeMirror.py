from tree_node import Tree


def mirror(node):
    if not node:
        return

    if node.lc:
        mirror(node.lc)

    if node.rc:
        mirror(node.rc)

    if node.has_child:
        temp = node.rc
        node.rc = node.lc
        node.lc = temp


if __name__ == '__main__':
    tree = Tree()
    tree.connect(4, 1, "L")
    tree.connect(4, 6, "R")
    tree.connect(1, 2, "R")
    tree.connect(2, 3, "R")
    tree.connect(6, 5, "L")
    tree.connect(6, 7, "R")

    tree.bfs()
    print("\n\n\n\n\n MIRROR\n\n\n")
    mirror(tree.head)
    tree.bfs()
