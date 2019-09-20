class Node(object):

    def __init__(self, value):
        self.lc = None
        self.rc = None
        self.p = None
        self.v = value

    @property
    def has_child(self):
        return self.lc or self.rc

    def __str__(self):
        return str(self.v)


class Tree(object):
    """
        Unique Number(un) of nodes
        Value of a node is different from un
        Generic Tree
    """
    def __init__(self):
        self.node_mapping = {}
        self.head = None

    def add(self, un, val):
        new_node = Node(val)
        if self.node_mapping.get(un) is not None:
            raise Exception("Unique Number is duplicate")
        self.node_mapping[un] = new_node
        if not self.head:
            self.head = new_node

    def connect(self, un1, un2, lr):
        if not self.node_mapping.get(un1):
            self.add(un1, un1)

        if not self.node_mapping.get(un2):
            self.add(un2, un2)

        if str(lr).lower() in ["left", "lc", "l", "0"]:
            self.node_mapping[un1].lc = self.node_mapping[un2]
        else:
            self.node_mapping[un1].rc = self.node_mapping[un2]

        self.node_mapping[un2].p = self.node_mapping[un1]

    def bfs(self):
        has_nodes = False
        if self.head:
            has_nodes = True
        node_list = [self.head, None]
        level = 0
        node_iter = iter(node_list)
        while has_nodes:
            has_nodes = False
            print("Level - %s"%level)
            try:
                node = next(node_iter)
                while node is not None:
                    print(node)
                    if node.lc:
                        has_nodes = True
                        node_list.append(node.lc)
                    if node.rc:
                        has_nodes = True
                        node_list.append(node.rc)
                    node = next(node_iter)
            except StopIteration:
                break
            node_list.append(None)
            level += 1
