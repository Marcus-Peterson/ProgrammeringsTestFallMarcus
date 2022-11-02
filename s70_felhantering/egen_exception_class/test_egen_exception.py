
from egen_exception import EgenException
from egen_exception import Kasta



assert issubclass(EgenException, Exception)

import unittest


class TestKastaException(unittest.TestCase):
    def test_kasta(self):
        with self.assertRaises(Exception):
            Kasta()

if __name__ == '__main__':
    unittest.main()