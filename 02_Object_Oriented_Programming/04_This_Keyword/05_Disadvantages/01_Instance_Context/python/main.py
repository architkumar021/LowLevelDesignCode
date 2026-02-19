from example import Example

# Calling static method
Example.display_message()  # Cannot access instance attributes

# Creating an instance to call an instance method
example = Example()
example.display_instance_message()  # Works fine

"""
Output:
Cannot access instance attributes in a static method
Hello, World!
"""

