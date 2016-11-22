import pandas as pd
import numpy as np
import scipy.io as sio

author = pd.read_csv('../author.txt', encoding='cp1252',sep=";")
print(author.head())

faculty= pd.read_csv('../scholars_faculty.csv', sep="\t")
print(faculty.head())

mat_contents = sio.loadmat('../coauthornet.mat')
coauthornet = mat_contents['coauthornet']
# Numpy NdArray

coauthor = pd.DataFrame(coauthornet,    # values
                        index=author['author name'],    # Names as index
                        columns=author['author name'])  # Names as column names

