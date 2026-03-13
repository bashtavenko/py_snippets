import unittest

from misc.ica.container import IntegerContainer


class ContainerTests(unittest.TestCase):
    failureException = Exception

    def setUp(self):
        self.container = IntegerContainer()

    def test_level_1_case_01_add_two_numbers(self):
        self.assertEqual(self.container.add(10), 1)
        self.assertEqual(self.container.add(100), 2)

    def test_level_1_case_02_add_many_numbers(self):
        self.assertEqual(self.container.add(10), 1)
        self.assertEqual(self.container.add(9), 2)
        self.assertEqual(self.container.add(8), 3)
        self.assertEqual(self.container.add(7), 4)
        self.assertEqual(self.container.add(6), 5)
        self.assertEqual(self.container.add(5), 6)
        self.assertEqual(self.container.add(4), 7)
        self.assertEqual(self.container.add(3), 8)
        self.assertEqual(self.container.add(2), 9)
        self.assertEqual(self.container.add(1), 10)

    def test_level_1_case_03_delete_number(self):
        self.assertEqual(self.container.add(10), 1)
        self.assertEqual(self.container.add(100), 2)
        self.assertTrue(self.container.delete(10))

    def test_level_1_case_04_delete_nonexisting_number(self):
        self.assertEqual(self.container.add(10), 1)
        self.assertEqual(self.container.add(100), 2)
        self.assertFalse(self.container.delete(20))
        self.assertTrue(self.container.delete(10))
        self.assertFalse(self.container.delete(10))

    def test_level_2_case_05_median_of_container_with_duplicates(self):
        self.assertEqual(self.container.add(5), 1)
        self.assertEqual(self.container.add(3), 2)
        self.assertEqual(self.container.add(5), 3)
        self.assertEqual(self.container.add(5), 4)
        self.assertEqual(self.container.add(10), 5)
        self.assertEqual(self.container.add(3), 6)
        self.assertEqual(self.container.get_median(), 5)
        self.assertEqual(self.container.add(3), 7)
        self.assertEqual(self.container.add(3), 8)
        self.assertEqual(self.container.add(3), 9)
        self.assertEqual(self.container.get_median(), 3)


if __name__ == '__main__':
    unittest.main()
