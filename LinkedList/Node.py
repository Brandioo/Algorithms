""" A simple Python program to introduce a linked list """


class Node:

    # Function to initialise the node object
    def __init__(self, data, next_node=None):
        self.data = data  # Assign data
        self.next = next_node  # Initialize next as null

    def __repr__(self):
        return str(self.data)


class LinkedList:

    # Function to initialize head
    def __init__(self, nodes: list['Node'] = None):
        self.head = None
        if nodes is not None:
            new_node = nodes.pop(0)
            self.head = new_node
            for node in nodes:
                new_node.next = Node(data=node.data)
                new_node = new_node.next

    # Function to represent the linked list
    def __repr__(self):
        node = self.head
        all_nodes = []
        while node is not None:
            all_nodes.append(str(node.data))
            node = node.next
        all_nodes.append("None")
        return " -> ".join(all_nodes)