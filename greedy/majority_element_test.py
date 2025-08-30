import unittest

import majority_element


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("a", majority_element.majority_search("bacaaabaac"))
        self.assertEqual("b", majority_element.majority_search("bbbbcaa"))


if __name__=="__main__":
    unittest.main()
