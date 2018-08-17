from unittest import TestCase

import example_pkg

class TestExample(TestCase):
    def test_is_string(self):
        s = example_pkg.example_function()
        self.assertTrue(isinstance(s, str))

class TestExample2(TestCase):
    def test_is_string(self):
        s = example_pkg.example_function2()
        self.assertTrue(isinstance(s, str))
