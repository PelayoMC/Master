import os
import pandas as pd
import numpy as np
from zlib import crc32

def load_data():
    csv_path = os.path.join(os.path.abspath(os.getcwd()), "airbnb.csv")
    return pd.read_csv(csv_path)
    
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    print('Datos separados')
    return data.iloc[train_indices], data.iloc[test_indices]