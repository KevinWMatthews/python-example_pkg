name = "example_pkg"

# This allows you to directly call:
# example_pkg.function_from_example_module()
from .example_module import function_from_example_module

# This requires you to call:
# example_pkg.example_module2.function_from_example_module2()
from . import example_module2

from . import example_class

# This function can be called using:
# example_pkg.function_from_init()
def function_from_init():
    return "Hello! This is an example function in __init__.py"
