import unittest
import requests
import datetime
import json
import validators
from lab_1.lr1.crawl import valid


class TestCrawler(unittest.TestCase):
    def setUp(self):
        self.url = 'https://3dnews.ru/'

    def test_valid(self):
        self.assertEqual(valid(self.url).status_code, 200)

if __name__='__main__':
    unittest.main()
