from unittest import TestCase, skip

import example_pkg
from example_pkg import example_module2

class TestInit(TestCase):
    def test_is_string(self):
        s = example_pkg.function_from_init()
        self.assertTrue(isinstance(s, str))

class TestExampleModule(TestCase):
    def test_is_string(self):
        s = example_pkg.function_from_example_module()
        self.assertTrue(isinstance(s, str))

class TestExampleModule2(TestCase):
    def test_is_string(self):
        s = example_module2.function_from_example_module2()
        self.assertTrue(isinstance(s, str))

import example_pkg.example_class
class TestExampleClass(TestCase):
    def test_init(self):
        example_pkg.example_class.ExampleClass()

class TestSyntaxExample(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @skip('Must put message here')
    def test_will_be_skipped(self):
        pass
