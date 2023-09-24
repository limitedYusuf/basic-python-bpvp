import unittest

def tambah(a, b):
    return a + b

# (test case)
class TestTambah(unittest.TestCase):
    def test_tambah_positif(self):
        self.assertEqual(tambah(2, 3), 5)

    def test_tambah_negatif(self):
        self.assertEqual(tambah(-2, -3), -5)

    def test_tambah_campuran(self):
        self.assertEqual(tambah(5, -3), 2)

if __name__ == '__main__':
    unittest.main()
