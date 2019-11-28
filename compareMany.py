import csv
from timeit import default_timer as timer
import lcs
import dp
import automata_test
import automata

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
for i in range(len(a)):
    # print(type(a[i]))
    result2 = lcs.editDistance(target_word,a[i])
    lcs1.append(result2)
end2 = timer()
lcsTime = end2 - start2

start3 = timer()
for i in range(len(a)):
    result3 = dp.dpEditDistance(target_word,a[i])
    dp1.append(result3)
end3 = timer()
dpTime = end3 - start3


print("The time taken for the automata to compute edit distance: ", automataTime)
print("The time taken for the lcs to compute edit distance: ", lcsTime)
print("The time taken for the dp to compute edit distance: ", dpTime)



    

