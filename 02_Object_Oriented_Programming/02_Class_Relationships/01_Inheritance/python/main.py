"""
Driver — demonstrates Inheritance (IS-A relationship).
Run: python main.py
"""

from dog import Dog


def main() -> None:
    dog = Dog("Buddy", "Golden Retriever")

    dog.eat()    # inherited from Animal
    dog.sleep()  # inherited from Animal
    dog.bark()   # Dog-specific

    print(dog)   # __str__


if __name__ == "__main__":
    main()

"""
Expected Output:
Buddy is eating.
Buddy is sleeping.
Buddy barks: Woof Woof!
Dog(Buddy, breed=Golden Retriever)
"""
