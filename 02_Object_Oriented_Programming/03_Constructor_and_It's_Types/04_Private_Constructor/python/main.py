from singleton import Singleton

s1 = Singleton.get_instance()
s2 = Singleton.get_instance()
print(s1 is s2)  # Output: True, as both references point to the same instance

"""
Output:
True
"""

