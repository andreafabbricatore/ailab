import pandas as pd
import numpy as np


def name_to_label(name):
    if "orm" in name:
        return 1
    elif "ypo" in name:
        return 0
    else:
        raise Exception


def add_label_T(df):
    df = df.T
    df["label"] = (df.index).map(name_to_label)
    return df


def calc_sparsity(matrix):
    sparsity = 1.0 - (np.count_nonzero(matrix) / float(matrix.size))

    return sparsity
