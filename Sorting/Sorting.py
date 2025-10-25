
class QuickSort:
    def __init__(self, arr):
        self.arr = arr
    
    def partition(self, low : int, high : int) -> int:
        pivot = self.arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                self.swap(i, j)
        i += 1
        self.swap(i, high)
        return i

    def swap(self, indx1 : int, indx2 : int):
        self.arr[indx1], self.arr[indx2] = self.arr[indx2], self.arr[indx1]
        
    def quickSort(self, low, high):
        if low < high:
            pivot = self.partition(low, high)
            self.quickSort(low, pivot - 1)
            self.quickSort(pivot + 1, high)
        

def selectionSort(arr : list[int]) -> list[int]:
    n = len(arr)
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr[mini] > arr[j]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr


def insertionSort(arr : list[int]) -> list[int]:
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0:
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
            j -= 1
    return arr

def BubbleSort(arr : list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr
                

def merge(arr : list[int], low : int, high : int, mid : int):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and  right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    while right <= high:
        temp.append(arr[right])
        right += 1
        
    for i in range(low, high + 1):
        arr[i] = temp[i - low]
        
def mergeSort(arr : list[int]):
    low, high = 0, len(arr) - 1
    
    def helper(arr, low, high):
        if low == high:
            return
        mid = low + (high - low) // 2
        helper(arr, low, mid)
        helper(arr, mid + 1, high)
        merge(arr, low, high, mid)
    helper(arr, low, high)
        
    
arr = [5, 4, 3, 2, 100, 1, 2, 3, 4, 5]
#mergeSort(arr)
sort = QuickSort(arr)
sort.quickSort(0, len(arr) - 1)
print(sort.arr)
    
    