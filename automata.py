from nfa import NFA


def levenshtein_automata(term, k):
    nfa = NFA((0, 0))
    for i, c in enumerate(term):
        for e in range(k + 1):
            # Correct character
            nfa.add_transition((i, e), c, (i + 1, e))
            if e < k:
                # Insertion
                nfa.add_transition((i, e), NFA.ANY, (i, e + 1))
                # Deletion
                nfa.add_transition((i, e), NFA.EPSILON, (i + 1, e + 1))
                # Substitution
                nfa.add_transition((i, e), NFA.ANY, (i + 1, e + 1))
    for e in range(k + 1):
        if e < k:
            nfa.add_transition((len(term), e), NFA.ANY, (len(term), e + 1))
        nfa.add_final_state((len(term), e))
    return nfa


def find_all_matches(word, k, lookup_func = False,test_word = False):

    print(test_word)
    """Uses lookup_func to find all words within levenshtein distance k of word.

    Args:
      word: The word to look up
      k: Maximum edit distance
      lookup_func: A single argument function that returns the first word in the
        database that is greater than or equal to the input argument.
    Yields:
      Every matching word within levenshtein distance k from the database.
    """

    print("[INFO]:In the automata function")
    #if test_word = True
    #we need to test a word
    if(test_word == True):
        #the word to be tested for is stored in k
        length = len(k)
        print("[INFO]: Testing the word {}".format(k))
        return
        
    else:
        print("HMMMMM")
        word = word.lower()
        print("WORD IS",word)
        lev = levenshtein_automata(word, k).to_dfa()
        match = lev.next_valid_string(u'\0')
        words_match = []

        #ADITYA AND MITHALI
        #IF I UNCOMMENT THE NEXT LINES, THE IF CASE STOPS WORKING FOR SOME BLOODY REASON
        # while match:
        #     next = lookup_func(match)
        #     if not next:
        #         return
        #     if match == next:
        #         #saving all the words at the edit distance
        #         words_match.append(next)
        #         yield match
        #         next = next + u'\0'
        #     match = lev.next_valid_string(next)

        # return words_match





    





        


    