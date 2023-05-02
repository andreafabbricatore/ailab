import pandas as pd


def name_to_label(name):
    if "orm" in name: return 1
    elif "ypo" in name: return 0
    else: raise Exception


def add_label_T(df, keep_name=False):
    df = df.T.reset_index(drop=False)
    df = df.rename(columns={"index": "name"})
    df["label"] = df["name"].apply(name_to_label)
    if not keep_name: df = df.drop("name", axis=1)
    return df
