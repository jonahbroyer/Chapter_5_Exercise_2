import unittest
from main import reverse


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_reverse(self):
        self.assertEqual(reverse([1, 2, 3, 5, 7]), [7, 5, 3, 2, 1])
