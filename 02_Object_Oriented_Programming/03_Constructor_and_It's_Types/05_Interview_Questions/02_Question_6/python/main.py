from example import Example

obj1 = Example(10)  # Valid value
obj1.display()
obj2 = Example(-5)  # Invalid value, constructor exits early
obj2.display()

"""
Output:
Value: 10
Invalid value! Constructor exiting early.
Value: 0
"""

