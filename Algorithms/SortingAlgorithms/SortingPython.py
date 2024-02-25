
# Basic Python implementation of common sorting algorithms
class SortingPython:

    # Bubble sort
    def BubbleSort(collection=[]):
        arr = list(collection)
        n = len(arr)
        if n < 2: # if array has less than 2 elements, it is already sorted
            return arr
        for i in range(n-1):
            sortedQ = True
            for j in range(n-1-i): # last i items are already sorted
                if arr[j+1] < arr[j]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    sortedQ = False
            if sortedQ: # if already sorted, stop the algorithm
                break
        return arr
    
    # Selection sort
    def SelectionSort(collection=[]):
        arr = list(collection)
        n = len(arr)
        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            if min_index == i: # if already sorted, stop the algorithm
                return arr
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
    
    # Insertion sort
    def InsertionSort(collection=[]):
        arr = list(collection)
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    # Shell sort
    def ShellSort(collection=[]):
        arr = list(collection)
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n): # iterate over all modulo classes
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp: # insertion sort
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr

if __name__ == '__main__':
    print(SortingPython.ShellSort([3, 7, 1, 9, 0, 8, 5, 6, 4, 2]))
