
import unittest
import sys
sys.path.append('DataStructures/Stack/Python/')

from StackPython import *

# Test class for StackPython
class test_StackPython(unittest.TestCase):
    # test_StackPython()
    def test___init__(self):
        # Case 1: No collection specified
        s1 = StackPython()
        self.assertEqual(s1.items, [])

        # Case 2: Collection specified
        s2 = StackPython([1, 2, 3])
        self.assertEqual(s2.items, [1, 2, 3])

    # test_is_empty()
    def test_is_empty(self):
        # Case 1: Stack is empty
        s1 = StackPython()
        self.assertEqual(s1.is_empty(), True)

        # Case 2: Stack is non-empty
        s2 = StackPython([1, 2, 3])
        self.assertEqual(s2.is_empty(), False)
    
    # test_push()
    def test_push(self):
        # Case 1: Stack is empty
        s1 = StackPython()
        s1.push('a')
        self.assertEqual(s1.items, ['a'])

        # Case 2: Stack is non-empty
        s2 = StackPython([1, 2, 3])
        s2.push(4)
        self.assertEqual(s2.items, [1, 2, 3, 4])

    # test_pop()
    def test_pop(self):
        # Case 1: Stack is non-empty
        s1 = StackPython([1, 2, 3])
        returned_item = s1.pop()
        self.assertEqual(returned_item, 3)
        self.assertEqual(s1.items, [1, 2])
    
    # test_peek()
    def test_peek(self):
        # Case 1: Stack is non-empty
        s1 = StackPython([1, 2, 3])
        returned_item = s1.peek()
        self.assertEqual(returned_item, 3)
        self.assertEqual(s1.items, [1, 2, 3])
    
    # test_size()
    def test_size(self):
        # Case 1: Stack is empty
        s1 = StackPython()
        self.assertEqual(s1.size(), 0)

        # Case 2: Stack is non-empty
        s2 = StackPython([1, 2, 3])
        self.assertEqual(s2.size(), 3)

if __name__ == '__main__':
    pass
