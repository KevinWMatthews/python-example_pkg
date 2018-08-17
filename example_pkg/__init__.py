name = "example_pkg"

# This allows you to directly call: example_pkg.example_function2()
from .example_module import example_function2

# This requires you to call: example_pkg.example_module.example_function2()
# from . import example_module

def example_function():
    return "Hello! This is an example function in __init__.py"
