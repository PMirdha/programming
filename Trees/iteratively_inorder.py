class Node:

    def __init__(self, v, parent=None):
        self.v = v
        self.lc = None
        self.rc = None
        self.parent = parent


def iteratively_inorder(p1: Node):
    btm = ""

    while p1:
        if p1.lc and not btm:
            p1 = p1.lc
            continue

        if not btm or btm == "left":
            print(p1.v)
            if p1.rc:
                p1 = p1.rc
                btm = ""
                continue

        btm = get_btm(p1)
        p1 = p1.parent


def get_btm(p):
    parent = p.parent
    if parent:
        if parent.lc == p:
            return "left"
        elif parent.rc == p:
            return "right"
    return ""


if __name__ == '__main__':
    n1 = Node(50)
    n2 = Node(10, n1)
    n3 = Node(60, n1)
    n1.lc = n2
    n1.rc = n3
    n4 = Node(8, n2)
    n5 = Node(40, n2)
    n2.lc = n4
    n2.rc = n5
    n6 = Node(20, n5)
    n5.lc = n6
    n7 = Node(15, n6)
    n8 = Node(30, n6)
    n6.lc = n7
    n6.rc = n8
    iteratively_inorder(n1)
