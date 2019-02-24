import unittest
from fastlang import FastLangDetect, iso_codes

class TestPolish(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestPolish, self).__init__(*args, **kwargs)
        self.lang = FastLangDetect()

    def test01(self):
        res = self.lang.detect('janusz i grażyna', k=1)
        self.assertEqual( res.keys()[0], 'pl' )

    def tes02(self):
        res = self.lang.detect('pies i kot w ogrodzie.', k=5)
        self.assertEqual( res.keys()[0], 'pl' )

    def test03(self):
        res = self.lang.detect('króliczek Koszi za 2 złote.', k=1)
        self.assertEqual( iso_codes[res.keys()[0]], 'Polish' )

if __name__ == '__main__':
    unittest.main()
