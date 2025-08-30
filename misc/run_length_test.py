import unittest

import run_length as m


class MyTestCase(unittest.TestCase):
    def test_example_1(self):
        result = m.decompress("ABRA KED\xFE\x34\x37")
        self.assertEqual("ABRA KEDABRA", result)

    def test_example_2(self):
        result = m.decompress("ABRA KED\xFE\x34\x37 \xFE\x35\x35")
        self.assertEqual("ABRA KEDABRA DABRA", result)


if __name__=="__main__":
    unittest.main()
