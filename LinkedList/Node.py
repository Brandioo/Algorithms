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

    def pop(self):
        # If there is only one element in the list
        if self.head.next is None:
            self.head = None
            return
        # Traverse the list until the node before the last node
        current_node = self.head
        while current_node.next:
            # Remove the pointer of the current node to the last node
            if current_node.next.next is None:
                current_node.next = None
                break
            # Continue iteration
            current_node = current_node.next

    def append(self, new_data):
        # If the LinkedList is empty, then make the new_node as head
        if self.head is None:
            self.push(new_data=new_data)
            return
        # Traverse the list till the last node
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        # Make the next of last node to the new last node
        current_node.next = Node(data=new_data, next_node=None)

    def insert_at(self, index: int, new_data):
        # Checking that index is valid
        if index not in list(range(0, len(self) + 1)):
            raise Exception('Index is invalid!')
        # If the index is 0 push the new node in the beginning
        if index == 0:
            self.push(new_data=new_data)
            return
        # Traverse the list till the node before desired position
        counter = 0
        current_node = self.head
        while current_node.next:
            if counter == index - 1:
                # Make the next of current node the new node
                # Make the next of new node the node that was after the current node
                new_node = Node(data=new_data, next_node=current_node.next)
                current_node.next = new_node
                break
            # Continue iteration
            current_node = current_node.next
            counter += 1

    def reverse(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:...
        self.head = previous_node
