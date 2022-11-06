import os
import pandas as pd

def load_data():
    csv_path = os.path.join(os.path.abspath(os.getcwd()), "airbnb.csv")
    return pd.read_csv(csv_path)