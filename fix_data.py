import pandas as pd


def name_to_label(name):
    if "orm" in name: return 1
    elif "ypo" in name: return 0
    else: raise Exception


def add_label_T(df):
    df = df.T
    df["label"] = (df.index).map(name_to_label)
    return df
