import automata
import bisect


#official dictionary of words
test_words = [x.strip().lower() for x in open('sowpods.txt')]
#user inputted words #we will check the distance of these words from the user specified target word
test_words = ["food","foid","foed","foeed","foeeed"]
test_words.sort()


def find_minimum_edits(target_word,test_word):
    length = len(test_word)
    # print("[INFO]: Testing the word {}".format(test_word))
    test_words = [test_word]
    valid = []
    for i in range(0,length+1):
        result_words = automata.find_all_matches(target_word,i,test_words)    
        if(len(list(result_words))!=0):
            valid.append(i)

    return min(valid)



if __name__ == '__main__':
    #this is your main function
    #we are calling everthing from here
    
    target_word = "food"
    target_distance = 2


    print("[STAGE]:Finding all words at a given edit distance")
    result_words = automata.find_all_matches(target_word,target_distance,test_words)
    print("[INFO]: The words to be tested:{} ".format((list(test_words))))
    print("[INFO]: The words at edit distance:{} ".format((list(result_words))))
    print("[INFO]: Stage Complete")

    print("\n \n")

    print("[STAGE]:Finding minimum edit distance for a word")
    test_word = "foooooooood"
    result = find_minimum_edits(target_word,test_word)
    print("[INFO]: Minimum number of edits to be made to convert {} into {} is: {}".format(test_word,target_word,result))
    print("[INFO]: Stage Complete")


