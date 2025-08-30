import unittest

import pretty_print as m

class PrettyPrintTestCase(unittest.TestCase):
    long_message = True

    def setUp(self):
        self.text = [
          'Lorem ipsum dolor sit amet.n',
          'amet dapibusin aenean.n']
        #  012345678912345678901234567890
        #            10        20       30

    def testWrap(self):
      result = m.simple_wrap(self.text, 13)
      expected = [
          'Lorem ipsum.n',
          'dolor sit.n',
          'amet.n',
          'amet .n',
          'dapibusin .n' ,
          'aenean.n']
      print 'Result:', result
      self.assertListEqual(expected, result)


    def testWrap_dp(self):
        words = ['aaa', 'bbb', 'c', 'd',
                 'ee', 'ff', 'ggggggg']
        self.assertEquals(19, m.calc_min_messiness(words, 10))


if __name__ == '__main__':
    unittest.main()
