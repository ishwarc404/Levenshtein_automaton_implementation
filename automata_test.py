import unittest
import automata
import bisect


words = [x.strip().lower() for x in open('sowpods.txt')]
words = ["food","foid","foed","foeed","foeeed"]
words.sort()


class Tests(unittest.TestCase):
    def test_food(self):
        m = Matcher(words)
        print("[INFO]: Number of words at edit distance:{} words".format(len((list(automata.find_all_matches('food', 2, m))))))
        # self.assertEqual(len((list(automata.find_all_matches('food', 1, m)))), 1)
        # self.assertEqual(len((list(automata.find_all_matches('food', 2, m)))), 2)

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
    unittest.main()
