import numpy as np
import string
import yaml

def increment(n):
    return n + 1

def min_max_scaler_bad(x):
    if x.size == 0:
        return x
    
    min = x.min()
    max = x.max()
    if min == max:
        scaler = lambda n: 0.5
    else:
        scaler = lambda n: (n-min) / (max - min)

    return np.array([scaler(xi) for xi in x])
    

def min_max_scaler(x):
    """
    Returns a numpy array with all of the original values scaled between 0 and 1.

    Assumes the data are a numpy array.
    """
    if x.size == 0:
        return x

    min = x.min()
    max = x.max()
    if min == max:
        return np.full(x.shape, 0.5)

    return (x - min) / (max - min)

def strip_punctuation(text):
    return ''.join(s for s in text if s not in string.punctuation)
    
def bag_of_words(text):
    return set(strip_punctuation(text).split())

def read_metadata(file):
    with open(file, 'r') as f:
        return yaml.load(f.read(), Loader=yaml.FullLoader)

def check_schema(df, meta_columns):
    for col in df.columns:
        assert col in meta_columns, f'"{col}" not in metadata column spec'


