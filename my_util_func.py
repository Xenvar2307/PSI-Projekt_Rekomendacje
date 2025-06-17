import pandas as pd

import faiss
import requests
import numpy as np

def create_textual_representation(row):
    textual_representation = f"""Type: {row['type']}
Title: {row['title']},
Director: {row['director']},
Cast: {row['cast']},
Year: {row['release_year']},
Genres: {row['listed_in']},

Description: {row['description']},
"""
    return textual_representation

def get_netflix_dataframe():
    df = pd.read_csv("netflix_titles.csv")

    df['textual_representation'] = df.apply(create_textual_representation, axis = 1)

    return df

def get_embedding_from_representation(representation):
    res = requests.post('http://localhost:11434/api/embeddings', 
                        json={
                            'model': 'llama2',
                            'prompt': representation
                        })
    
    embedding = np.array([res.json()['embedding']], dtype='float32')

    return embedding

