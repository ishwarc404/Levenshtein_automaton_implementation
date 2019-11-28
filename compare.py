from timeit import default_timer as timer
import lcs
import dp
import automata_test
import matplotlib.pyplot as plt
import numpy as np
# import matplotlib 
#compare lcs,dp and automata
print("[STAGE]:Finding minimum edit distance for a word")
target_word = "food"
test_word = "foooooooood"
start1 = timer()
result1 = automata_test.find_minimum_edits(target_word,test_word)
print(result1)
end1 = timer()
automataTime = end1 - start1

start2 = timer()
result2 = lcs.editDistance(target_word,test_word)
print(result2)
end2 = timer()
lcsTime = end2 - start2

start3 = timer()
result3 = dp.dpEditDistance(target_word,test_word)
print(result3)
end3 = timer()
dpTime = end3 - start3
# print("[INFO]: Minimum number of edits to be made to convert {} into {} is: {}".format(test_word,target_word,result))
# print("[INFO]: Stage Complete")
print("The time taken for the automata to compute edit distance: ", automataTime)
print("The time taken for the lcs to compute edit distance: ", lcsTime)
print("The time taken for the dp to compute edit distance: ", dpTime)

label = ['Levenshtein Automata', 'Least Common Subsequence', 'Dynamic Programming Approach']
times = [automataTime, lcsTime, dpTime]
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

