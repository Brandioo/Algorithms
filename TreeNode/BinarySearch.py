class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # node already exist

        if data < self.data:
            # add data in the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # then the value might be in the left subtree
            # condition to check if we have a left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # then the value might be in the right subtree
            # condition to check if we have a right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def pre_order_traversal(self):
        # add node data to the elements list
        elements = [self.data]

        if self.left:
            # visiting the left tree
            elements += self.left.pre_order_traversal()

        if self.right:
            # visiting the right tree
            elements += self.right.pre_order_traversal()

        return elements

    def in_order_traversal(self):
        elements = []
        if self.left:
            # visiting the left tree
            elements += self.left.in_order_traversal()

        # add node data to the elements list
        elements.append(self.data)

        if self.right:
            # visiting the right tree
            elements += self.right.in_order_traversal()

        return elements