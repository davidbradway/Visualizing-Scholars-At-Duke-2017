import pandas as pd
import scipy.io as sio
import numpy as np

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
        theircoauthors = get_coauthors(mycoauthor)
        mycocoauthors = pd.concat([mycocoauthors, theircoauthors], axis=1)

    return mycocoauthors, mycoauthors


def exclude_mine(mycocoauthors, mycoauthors):
    # Create an DataFrame for the results
    excluded = mycocoauthors.copy(deep=True)

    # For each coauthor, get *their* coauthors
    for mycoauthor, row in mycoauthors.iterrows():
        if mycoauthor in excluded.index:
            # remove it
            excluded.drop([mycoauthor], inplace=True)

    return excluded


if __name__ == "__main__":
    #me = 'Gregg E. Trahey'
    me = 'Kathryn Radabaugh Nightingale'
    mycocoauthors, mycoauthors = get_cocoauthors(me)

    excluded = exclude_mine(mycocoauthors, mycoauthors)
    excluded.drop([me], axis=1, inplace=True)

    transposed = excluded.T

    # Just look at number of people, not number of papers
    transposed[transposed > 0] = 1
    numbers = transposed.apply(np.sum)

    numbers.sort_values(inplace=True, ascending=False)
    top5 = numbers[:5]

    print(top5)