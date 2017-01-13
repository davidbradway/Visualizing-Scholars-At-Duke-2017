# http://lightning-viz.org/usage/#sharing

from lightning import Lightning
from numpy import random

lgn = Lightning(host='http://public.lightning-viz.org')

import pandas as pd
import numpy as np
import scipy.io as sio

from requests import get  # to make GET request

author = pd.read_csv('../author.txt', encoding='cp1252',sep=";")
#print(author.head())

faculty = pd.read_csv('../scholars_faculty.csv', sep="\t")
#print(faculty.head())

mat_contents = sio.loadmat('../coauthornet.mat')
coauthornet = mat_contents['coauthornet']
# Numpy NdArray

coauthor = pd.DataFrame(coauthornet,    # values
                        index=author['author name'],    # Names as index
                        columns=author['author name'])  # Names as column names

viz = lgn.force(coauthornet,labels=author['author name'])

# save it locally
# referenced from http://stackoverflow.com/a/34964610
def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)



#print(coauthornet[1103,1102])
#print(author.iloc[1103])
#print(author.iloc[1102])
temp = coauthornet[(1103,1102,2188,1551,1826,965,819,1105,1230,2013,2068,1591,36,230),:]
#print(temp.shape)
temp2 = temp[:,(1103,1102,2188,1551,1826,965,819,1105,1230,2013,2068,1591,36,230)]
#print(temp2)

tempauthor = author.iloc[[1103,1102,2188,1551,1826,965,819,1105,1230,2013,2068,1591,36,230],:]
#print(tempauthor.head())

# faculty[faculty['DUID']==tempauthor.iloc[8]['duke unique ID,']]['Appt Org Desc'].iloc[0]

label2 = []
depts = []
for i in range(tempauthor.shape[0]):
    depts.append(faculty[faculty['DUID']==tempauthor.iloc[i]['duke unique ID,']]['Appt Org Desc'].iloc[0])
    label2.append(tempauthor.iloc[i]['author name'] + ",\n " + faculty[faculty['DUID']==tempauthor.iloc[i]['duke unique ID,']]['Appt Org Desc'].iloc[0])
#print(label2)
#print(depts)

seen = []
depts_int = []
new = 1
# look at each department in the list
for i in range(len(depts)):
    # if we haven't seen it yet,
    if depts[i] not in seen:
        # add an integer to represent that department
        depts_int.append(new)
        # increment the integer that is used
        new = new + 1
        # add this department to the list of those that have been seen
        seen.append(depts[i])
    else:
        # else we did see it
        # get the first instance of this department, look up its integer, and append it
        depts_int.append(depts_int[depts.index(depts[i])])
#print(depts_int)
    

viz2 = lgn.force(temp2, labels=label2, group=depts_int)
viz3 = lgn.circle(temp2, labels=tempauthor['author name'], group=depts_int)

size_string = '/screenshot?width=800&height=600'

image_url = viz.get_permalink() + size_string
download(image_url, "force.png")

image_url = viz2.get_permalink() + size_string
download(image_url, "force_chain.png")

image_url = viz3.get_permalink() + size_string
download(image_url, "circle_chain.png")

