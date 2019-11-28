import lcs
import csv
# libraries and data
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


with open('data1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    d1 = list()
    for row in readCSV:
        for i in range(len(row)):
            d1.append(row[i])

with open('data2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    d2 = list()
    for row in readCSV:
        for i in range(len(row)):
            d2.append(row[i])

with open('data3.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    d3 = list()
    for row in readCSV:
        for i in range(len(row)):
            d3.append(row[i])

with open('data4.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    d4 = list()
    for row in readCSV:
        for i in range(len(row)):
            d4.append(row[i])


with open('data5.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    d5 = list()
    for row in readCSV:
        for i in range(len(row)):
            d5.append(row[i])

lcs1 = list()
lcs2 = list()
lcs3 = list()
lcs4 = list()
lcs5 = list()
target_word = "food"

start1 = timer()
for i in range(len(d1)-1):
    result1 = lcs.editDistance(target_word,d1[i])
    lcs1.append(result1)
end1 = timer()
timePasses1 = end1 - start1

start2 = timer()
for i in range(len(d2)-1):
    result2 = lcs.editDistance(target_word,d2[i])
    lcs2.append(result2)
end2 = timer()
timePasses2 = end2 - start2

start3 = timer()
for i in range(len(d3)-1):
    result3 = lcs.editDistance(target_word,d3[i])
    lcs3.append(result3)
end3 = timer()
timePasses3 = end3 - start3

start4 = timer()
for i in range(len(d4)-1):
    result4 = lcs.editDistance(target_word,d4[i])
    lcs4.append(result4)
end4 = timer()
timePasses4 = end4 - start4

start5 = timer()
for i in range(len(d5)-1):
    result5 = lcs.editDistance(target_word,d5[i])
    lcs5.append(result5)
end5 = timer()
timePasses5 = end5 - start5

x = [len(d1), len(d2), len(d3), len(d4), len(d5)]
y = [timePasses1, timePasses2, timePasses3, timePasses4, timePasses5]
df=pd.DataFrame({'xvalues': x, 'yvalues': y })
plt.xlabel('Input Size', fontsize=5)
plt.ylabel('LCS Running Time', fontsize=5) 
plt.title('Time v/s Varied Size input for the lCS algorithm')
# plot
plt.plot( 'xvalues', 'yvalues', data=df)
plt.show()