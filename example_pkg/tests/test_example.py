from unittest import TestCase

import example_pkg

class TestExample(TestCase):
    def test_is_string(self):
        s = example_pkg.example_function()
        self.assertFalse(isinstance(s, str))        # I print and don't return
