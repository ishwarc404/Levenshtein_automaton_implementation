import csv
from timeit import default_timer as timer
import lcs
import dp
import automata_test
import automata
import hamming
import matplotlib.pyplot as plt
import numpy as np

with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    a = list()
    for row in readCSV:
        for i in range(len(row)):
            a.append(row[i])
    # print(a)
target_word = "food"
auto=list()
lcs1 = list()
dp1 = list()
hamm = list()
k=5
start1 = timer()
for i in range(len(a)-1):
    result1 = automata_test.find_minimum_edits(target_word,a[i])
    # print(a[i])
    auto.append(result1)
end1 = timer()
automataTime = end1 - start1

# print(a[0])

start2 = timer()
for i in range(len(a)-1):
    # print(type(a[i]))
    result2 = lcs.editDistance(target_word,a[i])
    lcs1.append(result2)
end2 = timer()
lcsTime = end2 - start2

start3 = timer()
for i in range(len(a)-1):
    result3 = dp.dpEditDistance(target_word,a[i])
    dp1.append(result3)
end3 = timer()
dpTime = end3 - start3

start4 = timer()
for i in range(len(a)-1):
    result4 = hamming.hammingDistance(target_word,a[i])
    dp1.append(result4)
end4 = timer()
hammingTime = end4 - start4

# auto.sort()
# lcs1.sort()
# dp1.sort()
# print(len(auto)==len(lcs1)==len(dp1))
# print(auto==lcs1==dp1)
# print(auto)
# print(lcs1)
# print(dp1)
print("The time taken for the automata to compute edit distance: ", automataTime)
print("The time taken for the lcs to compute edit distance: ", lcsTime)
print("The time taken for the dp to compute edit distance: ", dpTime)
print("The time taken for the hamming to compute hamming distance: ", hammingTime)

label = ['Levenshtein Automata', 'Least Common Subsequence', 'Dynamic Programming Approach', 'Hamming Algorithm']
times = [automataTime, lcsTime, dpTime, hammingTime]
index = np.arange(len(label))
def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(label))
    plt.bar(index, times)
    plt.xlabel('Algorithm', fontsize=5)
    plt.ylabel('Time Taken in Seconds', fontsize=5)
    plt.xticks(index, label, fontsize=5, rotation=30)
    plt.title('Algorithms used to compute edit distance')
    plt.show()

plot_bar_x()

    

