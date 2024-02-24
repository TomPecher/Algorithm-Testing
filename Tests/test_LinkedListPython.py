
import unittest
import sys
sys.path.append('LinkedList/Python/')

from LinkedListPython import *

# Test class for LinkedListPython
class test_LinkedListPython(unittest.TestCase):
    # init()
    def test___init__(self):
        # Case 1: Initialise and empty linked list
        l1 = LinkedListPython()
        self.assertEquals(l1.head, None)

    # str()
    def test___str__(self):
        # Case 1: Linked list is empty
        l1 = LinkedListPython()
        self.assertEquals(str(l1), '')

        # Case 2: Linked list contains one item
        l2 = LinkedListPython()
        l2.insert('a')
        self.assertEquals(str(l2), 'a')

        # Case 3: Linked list contains several items
        l3 = LinkedListPython()
        l3.insert('a')
        l3.insert('b')
        l3.insert('c')
        self.assertEquals(str(l3), "a->b->c")

    # is_empty()
    def test_is_empty(self):
        # Case 1: Linked list is empty
        l1 = LinkedListPython()
        self.assertEquals(l1.is_empty(), True)

        # Case 2: Linked list contains items
        l2 = LinkedListPython()
        l2.insert('a')
        self.assertEquals(l2.is_empty(), False)
    
    # size()
    def test_size(self):
        # Case 1: Linked list is empty
        l1 = LinkedListPython()
        self.assertEquals(l1.size(), 0)

        # Case 2: Linked list contains one item
        l2 = LinkedListPython()
        l2.insert('a')
        self.assertEquals(l2.size(), 1)

        # Case 3: Linked list contains several items
        l3 = LinkedListPython()
        l3.insert('a')
        l3.insert('b')
        l3.insert('c')
        self.assertEquals(l3.size(), 3)
    
    # index(index)
    def test_index(self):
        l1 = LinkedListPython()
        l1.insert('a')
        l1.insert('b')
        l1.insert('c')

        # Case 1: Find index
        self.assertEquals(l1.index(0), 'a')
        self.assertEquals(l1.index(1), 'b')
        self.assertEquals(l1.index(2), 'c')
    
    # insert(index, item)
    def test_insert(self):
        l1 = LinkedListPython()
        l1.insert('b')
        l1.insert('d')

        # Case 1: Index not specified
        self.assertEquals(str(l1), "b->d")

        # Case 2: Index specified
        l1.insert('c', 1)
        self.assertEquals(str(l1), "b->c->d")

        # Case 3: Insert at start
        l1.insert('a', 0)
        self.assertEquals(str(l1), "a->b->c->d")
        self.assertEquals(l1.head.data, 'a')
    
    # delete(index)
    def test_delete(self):
        l1 = LinkedListPython()
        l1.insert('a')
        l1.insert('b')
        l1.insert('c')
        l1.insert('d')

        # Case 1: Delete middle item
        l1.delete(1)
        self.assertEquals(str(l1), "a->c->d")

        # Case 2: Delete end item
        l1.delete(2)
        self.assertEquals(str(l1), "a->c")

        # Case 3: Delete head
        l1.delete(0)
        self.assertEquals(str(l1), "c")
        self.assertEquals(l1.head.data, 'c')

if __name__ == '__main__':
    pass
