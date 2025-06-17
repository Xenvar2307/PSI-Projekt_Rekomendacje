import pandas as pd

import faiss
import requests
import numpy as np

#importing data

from my_util_func import get_netflix_dataframe, get_embedding_from_representation

df = get_netflix_dataframe()

#print(df['textual_representation'].values[0])

dim = 4096 # llama2 uses that size

index = faiss.IndexFlatL2(dim)
# flatL2 oblicza dokładnie odległości euklidesowe między wektorami, dokładny ale może być powolny

X = np.zeros((len(df['textual_representation']), dim), dtype='float32')

for i, representation in enumerate(df['textual_representation']):
    if i % 1 == 0:
        print(f'Done {i} rows.')
    
    embedding = get_embedding_from_representation(representation)

    X[i] = embedding


index.add(X)

faiss.write_index(index, 'index_1')