
def gnome_sort(lst: list[int]) -> list[int]:
    index = 0
    n = len(lst)

    while index < n:
        if index == 0:
            index += 1
        if lst[index] >= lst[index -1]:
            index += 1
        else:
            lst[index], lst[index -1] = lst[index - 1], lst[index]
            index -= 1

    return lst  