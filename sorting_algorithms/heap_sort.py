

def heapify(lst: list[int], n: int, i: int) -> None:
    largest: int = i
    left: int = 2 * i + 1
    right: int = 2 * i + 2

    if left < n and lst[left] > lst[largest]:
        largest = left

    if right < n and lst[right] > lst[largest]:
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]

        heapify(lst, n, largest)

def buildMaxHeap(lst) -> None:
    n: int = len(lst)
    for i in range(n // 2 - 1, -1, -1): 
        heapify(lst, n, i)

def heapSort(lst) -> list[int]:
    n: int = len(lst)
    buildMaxHeap(lst)

    for i in range(n -1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        n -= 1
        heapify(lst, n, 0)

    return lst