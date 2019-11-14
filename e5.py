import unittest
class TestMyProgram(unittest.TestCase):
    def test_upper(self):
        self.assertAlmostEqual('foo'.upper(),'FOO')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertTrue('FOO'.isupper())
if __name__ == '__main__':
    unittest.main()
