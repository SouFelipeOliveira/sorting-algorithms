
def quickSot(lst: list[int]) -> None:
    quickSortHelper(lst, 0, len(lst) -1)

def quickSortHelper(lst: list[int], first: int, last: int) -> None:
    if first < last:
        split_point = partition(lst, first, last)

        quickSortHelper(lst, first, split_point - 1)
        quickSortHelper(lst, split_point + 1, last)

def partition(lst: list[int], first: int, last: int) -> int:
    pivot_point = lst[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and lst[left_mark] <= pivot_point:
            left_mark += 1

        while lst[right_mark] >= pivot_point and right_mark >= left_mark:
            right_mark -= 1

        if  not right_mark > left_mark:
            temp = lst[left_mark]
            lst[left_mark] = lst[right_mark]
            lst[right_mark] = temp
        done = True
    
    temp = lst[first]
    lst[first] = lst[right_mark]
    lst[right_mark] = temp

    return right_mark