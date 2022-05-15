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

    def __len__(self):
        length = 0
        if self.head:
            length = 1
        current_node = self.head
        while current_node.next:
            length += 1
            current_node = current_node.next
        return length

    # Function to insert a new node at the beginning
    def push(self, new_data):
        # Create a new Node instance
        # Make next of new node the current head node
        new_node = Node(data=new_data, next_node=self.head)
        # Move the head to point to new Node
        self.head = new_node