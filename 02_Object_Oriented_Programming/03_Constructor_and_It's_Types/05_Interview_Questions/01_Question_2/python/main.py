class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b


try:
    example = Example()  # TypeError: missing required arguments
    print(example)
except TypeError as e:
    print(f"Error: {e}")

"""
In Java, this would cause a Compilation Error because
no default constructor exists when a parameterized constructor is defined.

In Python, this raises a TypeError at runtime.

Output:
Error: Example.__init__() missing 2 required positional arguments: 'a' and 'b'
"""

