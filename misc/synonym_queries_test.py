import unittest

import synonym_queries as m
import collections


TestItem = collections.namedtuple('TestItem', ('s1', 's2', 'result'))

class PangramTestCase(unittest.TestCase):
    long_message = True

    def setUp(self):
        self.test_items = [
          TestItem('major approval rate', 'major popularity rating', True),
          TestItem('major approval rates', 'major popularity rate', False),
          TestItem('major approval rate', 'popularity ratings major', False)]

    def testSynonyms(self):
        for i in self.test_items:
            self.assertEqual(i.result, m.is_synonym(
                i.s1.rsplit(' '),
                i.s2.rsplit(' ')))


if __name__ == '__main__':
    unittest.main()
