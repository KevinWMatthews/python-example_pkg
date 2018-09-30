import unittest
import example_pkg
from example_pkg import example_module2

class TestSyntaxExample(unittest.TestCase):
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

    @unittest.skip('Must put message here')
    def test_will_be_skipped(self):
        pass

class TestExampleClass(unittest.TestCase):
    def test_init(self):
        example_pkg.ExampleClass()

class TestInit(unittest.TestCase):
    def test_is_string(self):
        s = example_pkg.function_from_init()
        self.assertTrue(isinstance(s, str))

class TestExampleModule(unittest.TestCase):
    def test_is_string(self):
        s = example_pkg.function_from_example_module()
        self.assertTrue(isinstance(s, str))

class TestExampleModule2(unittest.TestCase):
    def test_is_string(self):
        s = example_module2.function_from_example_module2()
        self.assertTrue(isinstance(s, str))
