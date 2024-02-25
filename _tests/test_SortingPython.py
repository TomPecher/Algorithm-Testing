
import unittest
import sys
sys.path.append('Algorithms/SortingAlgorithms')

from SortingPython import *

# Test class for SortingPython
class test_SortingPython(unittest.TestCase):
    # test_BubbleSort()
    def test_BubbleSort(self):
        # Case 1: List is empty
        l1 = []
        self.assertEquals(SortingPython.BubbleSort(l1), [])

        # Case 2: List contains one item
        l2 = [1]
        self.assertEquals(SortingPython.BubbleSort(l2), [1])

        # Case 3: List contains multiple items
        l3 = [3, 7, 1, 9, 0, 8, 5, 6, 4, 2]
        self.assertEquals(SortingPython.BubbleSort(l3), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # test_SelectionSort()
    def test_SelectionSort(self):
        # Case 1: List is empty
        l1 = []
        self.assertEquals(SortingPython.SelectionSort(l1), [])

        # Case 2: List contains one item
        l2 = [1]
        self.assertEquals(SortingPython.SelectionSort(l2), [1])

        # Case 3: List contains multiple items
        l3 = [3, 7, 1, 9, 0, 8, 5, 6, 4, 2]
        self.assertEquals(SortingPython.SelectionSort(l3), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # test_InsertionSort()
    def test_InsertionSort(self):
        # Case 1: List is empty
        l1 = []
        self.assertEquals(SortingPython.InsertionSort(l1), [])

        # Case 2: List contains one item
        l2 = [1]
        self.assertEquals(SortingPython.InsertionSort(l2), [1])

        # Case 3: List contains multiple items
        l3 = [3, 7, 1, 9, 0, 8, 5, 6, 4, 2]
        self.assertEquals(SortingPython.InsertionSort(l3), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # test_ShellSort()
    def test_ShellSort(self):
        # Case 1: List is empty
        l1 = []
        self.assertEquals(SortingPython.ShellSort(l1), [])

        # Case 2: List contains one item
        l2 = [1]
        self.assertEquals(SortingPython.ShellSort(l2), [1])

        # Case 3: List contains multiple items
        l3 = [3, 7, 1, 9, 0, 8, 5, 6, 4, 2]
        self.assertEquals(SortingPython.ShellSort(l3), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
           

if __name__ == '__main__':
    pass
