


import unittest

import redpandas


class TestRedPanda(unittest.TestCase):

    def setUp(self):
        self.little_cochinardo = redpandas.RedPanda('Little Cochinardo', 3)

    def tearDown(self):
        pass

    def test_cute_words(self):
        something_cute = self.little_cochinardo.say_something_cute()
        self.assertEqual(something_cute, "<3<3<3")

    def test_cuteness_threshold(self):
        with self.assertRaises(ValueError):
            redpandas.RedPanda('Ugly Bob', 1)

    def test_cuteness_is_int(self):
        with self.assertRaises(TypeError):
            redpandas.RedPanda('Confused Marie', '5')



