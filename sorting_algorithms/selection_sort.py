from process_df import lst

def selectionSort(lst: list[int]) -> list[int]:
    for i in range(len(lst)-1, 0, -1):
        max_index: int = 0
        for j in range(1, i+1):
            if lst[j] > lst[max_index]:
                max_index = j
                lst[i], lst[max_index] = lst[max_index], lst[i]
    return lst