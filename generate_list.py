import pandas as pd
import random

sizes = [10, 50, 100, 200, 500, 800, 1000, 1500, 2000, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 10000]

def generate_list(size):
    list = random.sample(range(0, 10001), size)
    return list

def generate_xls(sizes):
    df = pd.DataFrame(index=range(max(sizes)), columns=sizes)
    for size in sizes:
        list = generate_list(size)
        df[size] = list[:size] + [None] * (max(sizes) - size)
        print(f'Generated list with {size} elements')
    df.to_excel('./db/list.xlsx')


generate_xls(sizes)