from unittest import TestCase

import example_pkg

class TestInit(TestCase):
    def test_is_string(self):
        s = example_pkg.function_from_init()
        self.assertTrue(isinstance(s, str))

class TestExampleModule(TestCase):
    def test_is_string(self):
        s = example_pkg.function_from_example_module()
        self.assertTrue(isinstance(s, str))
