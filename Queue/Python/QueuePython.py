
# Basic Python implementation of the queue data structure
class QueuePython:
    # init(collection)
    def __init__(self, collection=None):
        """Initialises an empty queue. If a collection is specified, initialises a queue with those items."""
        if collection:
            self.items = collection
        else:
            self.items = []

    # is_empty()
    def is_empty(self):
        """Returns True if queue contains no items, returns False otherwise."""
        return self.items == []
    
    # push(item)
    def enqueue(self, item):
        """Inserts the specified item at the end of the queue."""
        self.items.append(item)

    # pop()
    def dequeue(self):
        """Returns the item at the end of the queue (if it exists), removing it in the process."""
        if self.is_empty():
            raise IndexError("Popping from empty queue")
        return self.items.pop(0)
    
    # peek()
    def peek(self):
        """Returns the item at the end of the queue (if it exists)."""
        if self.is_empty():
            raise IndexError("Peeking onto empty queue")
        return self.items[0]
    
    # size()
    def size(self):
        """Returns the number of elements in the queue."""
        return len(self.items)

if __name__ == '__main__':
    pass
