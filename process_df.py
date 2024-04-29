import pandas as pd
import time

import imports

df = pd.read_excel('./db/list.xlsx', index_col=0)

def process_df(df):
    for column in df.columns:
        lst = df[column].dropna().tolist()
        
        start_time = time.time()
        imports.selectionSort(lst) # Change this line to algorithm of your choice
        end_time = time.time()
        
        print(f'List with {len(lst)} elements')
        print(f'Time taken: {end_time - start_time} seconds')

process_df(df)