import unittest
from lab_1.lr1.crawl import valid

class TestCrawler(unittest.TestCase):
    def setUp(self):
        self.url = 'https://3dnews.ru/'
        self.incorrect_url = 'https://3dnews.ru/asdassaaa'

    def test_valid(self):
        self.assertEqual(valid(self.url).status_code, 200)
    
    def test_valid(self):
        self.assertEqual(valid(self.incorrect_url).status_code, 404)
