import unittest


class TestKastaException(unittest.TestCase):
    def test_kasta(self):
        with self.assertRaises(Exception):
            import kasta_exception

if __name__ == '__main__':
    unittest.main()