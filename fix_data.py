import pandas as pd


def name_to_label(name):
    if "orm" in name: return 1
    elif "ypo" in name: return 0
    else: raise Exception


def add_label_T(df, dropname=False):
    df = df.T
    df["label"] = (df.index).map(name_to_label)
    if dropname:
        df = df.reset_index(drop=True)
    return df
