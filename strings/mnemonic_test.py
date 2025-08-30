"""Tests for strings bootcamp."""

import unittest

import mnemonic


class MnemonicTestCase(unittest.TestCase):
    def testMnemonic(self):
        result = mnemonic.phone_mnemonic("2276696")
        self.assertEqual(3888, len(result))

    def testMnemonicSingle(self):
        result = mnemonic.phone_mnemonic("2")
        self.assertListEqual(["A", "B", "C"], result)

    def testMnemonicDouble(self):
        result = mnemonic.phone_mnemonic("23")
        self.assertListEqual(
            ["AD", "AE", "AF", "BD", "BE", "BF", "CD", "CE", "CF"], result
        )


if __name__=="__main__":
    unittest.main()
