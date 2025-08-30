"""Tests for crawler."""
import unittest

import crawler as m

class CrawlerTestCase(unittest.TestCase):

    def testCrawl(self):
        result = m.crawl('u1')
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
