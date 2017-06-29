import unittest
from mylevenshtein import mylevenshtein
import distance
import time

class Testmylevenshtein(unittest.TestCase):

    t = ['Print', 'Yesterday', 'All', 'my', 'troubles', 'seemed so far away',
         'Now it looks as though they', 're here to stay',
         'Oh, I believe in yesterday',
         'Suddenly,',
         'I', 'm not half the man I used to be',
         'There', 's a shadow hanging over me',
         'Oh, yesterday came suddenly']
    scale = 100

    def test_correct_ldistance(self):
        l = mylevenshtein()
        self.assertEqual(distance.levenshtein("1234", "1243"), l.ldistance("1234", "1243"))

    def test_correct_big_ldistance(self):
        l = mylevenshtein()
        for i in range(len(self.t) - 1):
            self.assertEqual(distance.levenshtein(self.t[i], self.t[i + 1]), l.ldistance(self.t[i], self.t[i + 1]))

    def test_speed_big_ldistance(self):
        l = mylevenshtein()
        start = time.time()
        for j in range(0, self.scale):
            for i in range(len(self.t) - 1):
                distance.levenshtein(self.t[i], self.t[i + 1])
        pause = time.time()
        for j in range(0, self.scale):
            for i in range(len(self.t) - 1):
                l.ldistance(self.t[i], self.t[i + 1])
        end = time.time()
        self.assertTrue((start - pause) < (pause - end), "my distance is faster than levenstein in " + str(((start - pause)/(pause - end))) + " times")
        print("my distance is slower than levenstein module in " + str(((start - pause)/(pause - end))) + " times")


if __name__ == '__main__':
    unittest.main()
