import pandas as pd
import scipy.io as sio
# import numpy as np

author = pd.read_csv('../author.txt', encoding='cp1252', sep=";")
# print(author.head())

faculty = pd.read_csv('../scholars_faculty.csv', sep="\t")
# print(faculty.head())

mat_contents = sio.loadmat('../coauthornet.mat')
coauthornet = mat_contents['coauthornet']
# Numpy NdArray

coauthornetDF = pd.DataFrame(coauthornet,    # values
                             index=author['author name'],    # Names as index
                             columns=author['author name'])  # Names as column names
# print(coauthor.head(2))

"""
With whom should I be collaborating? Suggest Facebook friends
Select all of my coauthors by name or key. (each non zero entry in my row)
Select all their coauthors
filter out those who were my coauthors
Rank the remaining coauthors by the number of papers my coauthors published with them
"""
# coauthor['Gregg E. Trahey']['Kathryn Radabaugh Nightingale']


def get_coauthors(name):
    coauthors = coauthornetDF.loc[coauthornetDF[name] > 0, [name]]
    return coauthors


def get_cocoauthors(name):
    mycoauthors = get_coauthors(name)

    # Create an empty DataFrame for the results
    mycocoauthors = pd.DataFrame()

    # For each coauthor, get *their* coauthors
    for mycoauthor, row in mycoauthors.iterrows():
        # print(index)
        theircoauthors = get_coauthors(mycoauthor)
        mycocoauthors = pd.concat([mycocoauthors, theircoauthors], axis=1)

    return mycocoauthors, mycoauthors


if __name__ == "__main__":
    mycocoauthors, mycoauthors = get_cocoauthors('Gregg E. Trahey')



    print('end')