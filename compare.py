from timeit import default_timer as timer
import lcs
import dp
import automata_test
# import matplotlib 
#compare lcs,dp and automata
print("[STAGE]:Finding minimum edit distance for a word")
target_word = "food"
test_word = "foooooooood"
start1 = timer()
result = automata_test.find_minimum_edits(target_word,test_word)
end1 = timer()
automataTime = end1 - start1

start2 = timer()
result = lcs.editDistance(target_word,test_word)
end2 = timer()
lcsTime = end2 - start2

start3 = timer()
result = dp.dpEditDistance(target_word,test_word)
end3 = timer()
dpTime = end3 - start3
# print("[INFO]: Minimum number of edits to be made to convert {} into {} is: {}".format(test_word,target_word,result))
# print("[INFO]: Stage Complete")
print("The time taken for the automata to compute edit distance: ", automataTime)
print("The time taken for the lcs to compute edit distance: ", lcsTime)
print("The time taken for the dp to compute edit distance: ", dpTime)

