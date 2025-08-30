import math
import random
import unittest

import bootcamp


class BootcampTestCase(unittest.TestCase):

    def testCountBits(self):
        self.assertEqual(2, bootcamp.count_ones(5))
        self.assertEqual(3, bootcamp.count_ones(7))

        self.assertEqual(2, bootcamp.count_ones_plus(5))
        self.assertEqual(3, bootcamp.count_ones_plus(7))

    def testXor(self):
        """
        Bits are different 0-0=0 / 0-1=1 / 1-0=1/1-1=0
        XOR of two bits == mod 2
        """
        self.assertEqual(0, 3 ^ 3)
        self.assertEqual(3, 3 ^ 0)
        # Flips the bit.
        # This can be used to increment count
        # c ^= 1 instead of c = c + 1 or c += 1
        # Useful - the count never goes higher than base + 1
        # That is: if c = 0, it can be 0 or 1, if c = 1, it is 1 or 2
        self.assertEqual(2, 3 ^ 1)

        """
        Since every number xor'd with itself gives zero and any number xor'd
        with zero gives itself, it's easy to find a number that occurs once:
        """
        self.assertEqual(2, 1 ^ 1 ^ 2 ^ 3 ^ 3 ^ 4 ^ 4)

    def testPrimitives(self):
        # 2 1 1
        # 4 2 1
        # Start with 1
        self.assertEqual(5, bootcamp.set_bit(1, 2))
        self.assertEqual(1, bootcamp.reset_bit(5, 2))
        self.assertTrue(bootcamp.test_bit(3, 1))
        self.assertFalse(bootcamp.test_bit(3, 2))

        self.assertEqual(7, bootcamp.toggle(3, 2))

        # 8421
        # 1100 (12) => 8
        self.assertEqual(8, bootcamp.turn_off_right_most_one(12))

    def testBasicTypes(self):
        self.assertEqual(3, math.ceil(2.17))
        self.assertEqual(2, math.floor(2.17))
        self.assertEqual(2, min(5, 2))
        self.assertEqual("42", str(42))
        self.assertEqual(42, int("42"))
        self.assertEqual(3.14, float("3.14"))
        self.assertGreater(10, random.randrange(10))
        self.assertLess(1, random.randint(2, 10))
        # Also: random.choice[list], random.shuffle(a)
        self.assertEqual(-3, ~2)  # Complement

    def basic_looping(self):
        # Since Python doesn't have for (i = 1, ...) loop ..
        # range doesn't include upper bound which is good in for loop
        a = ["a", "b", "c", "d"]
        for i in range(0, len(a)):
            print(a[i])

    def testDigitsOfTheNumber(self):
        number = 329
        self.assertEqual(3, bootcamp.get_digits_of_number(number, 2))
        self.assertEqual(2, bootcamp.get_digits_of_number(number, 1))
        self.assertEqual(9, bootcamp.get_digits_of_number(number, 0))


if __name__ == "__main__":
    unittest.main()
