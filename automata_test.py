# import unittest
import automata
import bisect


#official dictionary of words
words = [x.strip().lower() for x in open('sowpods.txt')]
#user inputted words #we will check the distance of these words from the user specified target word
words = ["food","foid","foed","foeed","foeeed"]
words.sort()


# class Tests(unittest.TestCase):
#     def test_main(self):
#         # self.assertEqual(len((list(automata.find_all_matches('food', 1, m)))), 1)
#         # self.assertEqual(len((list(automata.find_all_matches('food', 2, m)))), 2)
#         #will edit this part later
#         pass

class Matcher(object):
    def __init__(self, l):
        self.l = l
        self.probes = 0

    def __call__(self, w):
        self.probes += 1
        pos = bisect.bisect_left(self.l, w)
        if pos < len(self.l):
            return self.l[pos]
        else:
            return None


if __name__ == '__main__':
    #this is your main function
    #we are calling everthing from here
    m = Matcher(words)
    target_word = "FOOD"
    target_distance = 2

    #When the 4th parameter is false, we are just checking which words are at an edited distance
    #When true, we are going to check what are the minimum number of edits to make
    result_words = automata.find_all_matches(target_word,target_distance,m,test_word = False)
    print("[INFO]: The words at edit distance:{} ".format((list(result_words))))
    print("DONE")


    #When true
    #replacing the (2nd) distance paramter with word to test for
    result = automata.find_all_matches(target_word,"fooooooood",lookup_func = False,test_word = True)
    print("DONE")

    #NOTE: CHECK THIS OUT, FOR SOME REASON IT IS NOT EXECUTING
