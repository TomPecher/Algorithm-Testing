
# Basic Python implementation of the Stack data structure
class StackPython:
    # init(collection)
    def __init__(self, collection=[]):
        """Initialises an empty stack. If a collection is specified, initialises a stack with those items."""
        self.items = collection

    # is_empty()
    def is_empty(self):
        """Returns True if stack contains no items, returns False otherwise."""
        return self.items == []
    
    # push(item)
    def push(self, item):
        """Inserts the specified item at the end of the stack."""
        self.items.append(item)

    # pop()
    def pop(self):
        """Returns the item at the end of the stack (if it exists), removing it in the process."""
        if self.is_empty():
            raise IndexError("Popping from empty stack")
        return self.items.pop()
    
    # peek()
    def peek(self):
        """Returns the item at the end of the stack (if it exists)."""
        if self.is_empty():
            raise IndexError("Peeking onto empty stack")
        return self.items[-1]
    
    # size()
    def size(self):
        """Returns the number of elements in the stack."""
        return len(self.items)
