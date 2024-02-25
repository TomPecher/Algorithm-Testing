
# Node class
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data

# Basic Python implementation of the linked list data structure
class LinkedListPython:
    # init()
    def __init__(self):
        """Initialises an empty linked."""
        self.head = None

    # str()
    def __str__(self):
        """Convert to string."""
        # If empty, return empty string
        if not self.head:
            return ''
        # Else, collect data of all nodes in a list and join
        l = []
        current_node = self.head
        while current_node:
            l.append(str(current_node))
            current_node = current_node.next
        return "->".join(l)

    # is_empty()
    def is_empty(self):
        """Returns True if linked list contains no items, returns False otherwise."""
        return self.head == None
    
    # size()
    def size(self):
        """Returns the number of elements in the linked list."""
        i = 0
        current_node = self.head
        while(current_node != None):
            current_node = current_node.next
            i+=1
        return i
    
    # index(index)
    def index(self, index):
        """Returns the item at the specified index position (if it exists)."""
        if index < 0 or index >= self.size():
            raise IndexError("Index out of range.")
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.data
    
    # insert(index, item)
    def insert(self, data, index=-1):
        """Inserts the specified item at the specified index position (if possible). If no position is specified, insert at the end."""
        new_node = Node(data)
        if index < -1 or index > self.size():
            raise IndexError("Index out of range.")
        elif index == -1:
            index = self.size()

        if index == 0:
            if self.head is not None:
                new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
    
    # delete(index)
    def delete(self, index):
        """Deletes the item (node) at the specified index position (if it exists)."""
        if index < 0 or index >= self.size():
            raise IndexError("Index out of range.")
        previous_node = None
        current_node = self.head
        for _ in range(index):
            previous_node = current_node
            current_node = current_node.next

        if index == 0:
            self.head = current_node.next
        else:
            previous_node.next = current_node.next
        del current_node

if __name__ == '__main__':
    pass
