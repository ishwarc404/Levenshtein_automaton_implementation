from nfa import NFA
import bisect


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



def find_minimum_edits(target_word, k,test_words):
    #lookup function
    lookup_func = Matcher(test_words)

    target_word = target_word.lower()
    lev = levenshtein_automata(target_word, k).to_dfa()
    match = lev.next_valid_string(u'\0')
    words_match = []
    #ADITYA AND MITHALI
    #IF I UNCOMMENT THE NEXT LINES, THE IF CASE STOPS WORKING FOR SOME BLOODY REASON
    while match:
        next = lookup_func(match)
        if not next:
            return
        if match == next:
            #saving all the words at the edit distance
            words_match.append(next)
            yield match
            next = next + u'\0'
        match = lev.next_valid_string(next)

    return words_match




def find_all_matches(target_word, k,test_words):


    """Uses lookup_func to find all words within levenshtein distance k of word.
    Args:
      word: The word to look up
      k: Maximum edit distance
      lookup_func: A single argument function that returns the first word in the
        database that is greater than or equal to the input argument.
    Yields:
      Every matching word within levenshtein distance k from the database.
    """

    #lookup function
    lookup_func = Matcher(test_words)

    target_word = target_word.lower()
    lev = levenshtein_automata(target_word, k).to_dfa()
    match = lev.next_valid_string(u'\0')
    words_match = []
    #ADITYA AND MITHALI
    #IF I UNCOMMENT THE NEXT LINES, THE IF CASE STOPS WORKING FOR SOME BLOODY REASON
    while match:
        next = lookup_func(match)
        if not next:
            return
        if match == next:
            #saving all the words at the edit distance
            words_match.append(next)
            yield match
            next = next + u'\0'
        match = lev.next_valid_string(next)

    return words_match





    





        


    