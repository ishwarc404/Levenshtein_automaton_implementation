import automata_test
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

auto1 = list()
auto2 = list()
auto3 = list()
auto4 = list()
auto5 = list()
target_word = "food"

start1 = timer()
for i in range(len(d1)-1):
    result1 = automata_test.find_minimum_edits(target_word,d1[i])
    auto1.append(result1)
end1 = timer()
timePasses1 = end1 - start1

start2 = timer()
for i in range(len(d2)-1):
    result2 = automata_test.find_minimum_edits(target_word,d2[i])
    auto2.append(result2)
end2 = timer()
timePasses2 = end2 - start2

start3 = timer()
for i in range(len(d3)-1):
    result3 = automata_test.find_minimum_edits(target_word,d3[i])
    auto3.append(result3)
end3 = timer()
timePasses3 = end3 - start3

start4 = timer()
for i in range(len(d4)-1):
    result4 = automata_test.find_minimum_edits(target_word,d4[i])
    auto4.append(result4)
end4 = timer()
timePasses4 = end4 - start4

start5 = timer()
for i in range(len(d5)-1):
    result5 = automata_test.find_minimum_edits(target_word,d5[i])
    auto5.append(result5)
end5 = timer()
timePasses5 = end5 - start5

x = [len(d1), len(d2), len(d3), len(d4), len(d5)]
y = [timePasses1, timePasses2, timePasses3, timePasses4, timePasses5]
df=pd.DataFrame({'xvalues': x, 'yvalues': y })
plt.xlabel('Input Size', fontsize=5)
plt.ylabel('Levenshetein Automata Running Time', fontsize=5) 
plt.title('Time v/s Varied Size input for the algorithm')
# plot
plt.plot( 'xvalues', 'yvalues', data=df)
plt.show()