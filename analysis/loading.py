import pandas as pd

def data_load(filepath):
    df=pd.read_csv(filepath)
    return df