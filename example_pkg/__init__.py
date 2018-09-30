name = "example_pkg"

# This allows you to directly call:
# example_pkg.function_from_example_module()
from .example_module import function_from_example_module

# This requires you to call:
# example_pkg.example_module2.function_from_example_module2()
from . import example_module2

# This makes the example_class module accessible after importing example_pkg
# Must call example_pkg.example_class.ExampleClass
# from . import example_class

# This makes ExampleClass accessible after importing example_pkg
# Can call example_pkg.ExampleClass
from .example_class import ExampleClass


# This function can be called using:
# example_pkg.function_from_init()
def function_from_init():
    return "Hello! This is an example function in __init__.py"
