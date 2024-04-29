
def insertionSort(lst: list[int]) -> list[int]:
    for i in range(1, len(lst)):
        key: int = lst[i]
        position: int = i
        while position > 0 and lst[position-1] > key:
            lst[position] = lst[position-1]
            position -= 1
        lst[position] = key
    return lst