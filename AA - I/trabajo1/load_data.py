import os
import pandas as pd
import numpy as np
from zlib import crc32

def load_data():
    csv_path = os.path.join(os.path.abspath(os.getcwd()), "airbnb.csv")
    return pd.read_csv(csv_path)
    
def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32

def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]