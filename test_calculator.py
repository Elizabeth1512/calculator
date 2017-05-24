import unittest
from Calculator import *
class TestZERO(unittest.TestCase):
    def test_value(self):
        init = start()
        init("1/0")
        result = init("=")
        self.assertEqual("Error", result)

if __name__ == '__main__':
    unittest.main()