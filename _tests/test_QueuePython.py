
import unittest
import sys
sys.path.append('DataStructures/Queue/Python/')

from QueuePython import *

# Test class for QueuePython
class test_QueuePython(unittest.TestCase):
    # test_QueuePython()
    def test___init__(self):
        # Case 1: No collection specified
        s1 = QueuePython()
        self.assertEqual(s1.items, [])

        # Case 2: Collection specified
        s2 = QueuePython([1, 2, 3])
        self.assertEqual(s2.items, [1, 2, 3])

    # test_is_empty()
    def test_is_empty(self):
        # Case 1: Queue is empty
        s1 = QueuePython()
        self.assertEqual(s1.is_empty(), True)

        # Case 2: Queue is non-empty
        s2 = QueuePython([1, 2, 3])
        self.assertEqual(s2.is_empty(), False)
    
    # test_ensqueue()
    def test_enqueue(self):
        # Case 1: Queue is empty
        s1 = QueuePython()
        s1.enqueue('a')
        self.assertEqual(s1.items, ['a'])

        # Case 2: Queue is non-empty
        s2 = QueuePython([1, 2, 3])
        s2.enqueue(4)
        self.assertEqual(s2.items, [1, 2, 3, 4])

    # test_dequeue()
    def test_dequeue(self):
        # Case 1: Queue is non-empty
        s1 = QueuePython([1, 2, 3])
        returned_item = s1.dequeue()
        self.assertEqual(returned_item, 1)
        self.assertEqual(s1.items, [2, 3])
    
    # test_peek()
    def test_peek(self):
        # Case 1: Queue is non-empty
        s1 = QueuePython([1, 2, 3])
        returned_item = s1.peek()
        self.assertEqual(returned_item, 1)
        self.assertEqual(s1.items, [1, 2, 3])
    
    # test_size()
    def test_size(self):
        # Case 1: Queue is empty
        s1 = QueuePython()
        self.assertEqual(s1.size(), 0)

        # Case 2: Queue is non-empty
        s2 = QueuePython([1, 2, 3])
        self.assertEqual(s2.size(), 3)

if __name__ == '__main__':
    pass
