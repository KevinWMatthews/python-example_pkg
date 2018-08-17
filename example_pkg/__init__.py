name = "example_pkg"

# This allows you to directly call:
# example_pkg.function_from_example_module()
from .example_module import function_from_example_module

# This function can be called using:
# example_pkg.function_from_init()
def function_from_init():
    return "Hello! This is an example function in __init__.py"
