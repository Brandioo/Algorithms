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

    def remove_at(self, index: int):
        # Checking that index is valid
        if index not in range(0, len(self) + 1):
            raise Exception('Index is invalid!')
        # If index is equal to the linked list length
        if index == len(self):
            self.pop()
            return
        # If index is at the first element
        if index == 0:
            self.head = self.head.next
            return
            # Traverse the list till the node before desired position
        counter = 0
        current_node = self.head
        while current_node.next:
            if counter == index - 1:
                current_node.next = current_node.next.next
                break

            current_node = current_node.next
            counter += 1

    def insert_after(self, index: int, new_data):
        # Checking that index is valid
        if index not in list(range(0, len(self) + 1)):
            raise Exception('Index is invalid!')
        # If the index is equal to length of list
        # append the new node in the end
        if index == len(self):
            self.append(new_data=new_data)
            return
        # Traverse the list till the node at desired position
        counter = 0
        current_node = self.head
        while current_node.next:
            if counter == index:
                # Make the next of current node the new node
                # Make the next of new node the node that was after the current node
                new_node = Node(data=new_data, next_node=current_node.next)
                current_node.next = new_node
                break
            # Continue iteration
            current_node = current_node.next
            counter += 1

    def reverse(self):
        # Function to reverse the linked list
        previous_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def swap_nodes(self, x, y):

        # Nothing to do if x and y are same
        if x == y:
            return

        # Search for x (keep track of prevX and CurrX)
        prev_x = None
        curr_x = self.head
        while curr_x is not None and curr_x.data != x:
            prev_x = curr_x
            curr_x = curr_x.next

        # Search for y (keep track of prevY and currY)
        prev_y = None
        curr_y = self.head
        while curr_y is not None and curr_y.data != y:
            prev_y = curr_y
            curr_y = curr_y.next

        # If either x or y is not present, nothing to do
        if curr_x is None or curr_y is None:
            return
        # If x is not head of linked list
        if prev_x is not None:
            prev_x.next = curr_y
        else:  # make y the new head
            self.head = curr_y

        # If y is not head of linked list
        if prev_y is not None:
            prev_y.next = curr_x
        else:  # make x the new head
            self.head = curr_x

        # Swap next pointers
        temp = curr_x.next
        curr_x.next = curr_y.next
        curr_y.next = temp


if __name__ == '__main__':
    # Creating the new nodes
    new_nodes = [Node("a"), Node("b"), Node("c")]
    # Creating the linked list instance
    linked_list = LinkedList(nodes=new_nodes)
    print(linked_list)
    print(f"Length of Linked List is : {len(linked_list)}")

    # Insert a new node at the beginning
    linked_list.push('d')
    print(linked_list)

    # Insert a new node at the end
    linked_list.append('e')
    print(linked_list)

    # Insert a new node at position 1
    linked_list.insert_at(1, 'f')
    print(linked_list)

    # Insert a new node after position 1
    linked_list.insert_after(2, '1')
    print(linked_list)

    # Remove the last element
    linked_list.pop()
    print(linked_list)

    # Remove element at position 5
    linked_list.remove_at(3)
    print(linked_list)

    # Remove element at the beginning
    linked_list.remove_at(0)
    print(linked_list)

    # Reverse the list
    linked_list.reverse()
    print(linked_list)

    # Swap nodes
    linked_list.swap_nodes('b', 'f')
    print(linked_list)