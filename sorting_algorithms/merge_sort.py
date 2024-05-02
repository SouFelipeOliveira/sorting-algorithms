
def mergeSort(lst: list[int]) -> None:
    if len(lst) > 1:
        mid: int = len(lst)//2
        left: list[int] = lst[:mid]
        right: list[int] = lst[mid:]


        mergeSort(left)
        mergeSort(right)

        j=j=k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k]=lst[i]
                i+=1
            else:
                lst[k]=right[j]
                j+=1
            k+=1

        while i < len(left):
                lst[k]=left[i]
                i+=1
                k+=1

        while j < len(right):
             lst[k]=right[j]
             j+=1 
             k+=1        