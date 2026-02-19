"""
Driver — demonstrates Dependency (USES-A temporarily).
Run: python main.py
"""

from document import Document
from printer import Printer


def main() -> None:
    doc = Document("Report", "Hello, World!")
    office_printer = Printer("Office HP")
    home_printer = Printer("Home Canon")

    # Same document, different printers — dependency is temporary
    doc.print_document(office_printer)
    print()
    doc.print_document(home_printer)


if __name__ == "__main__":
    main()

"""
Expected Output:
Document: Report
[Office HP] Printing: Hello, World!

Document: Report
[Home Canon] Printing: Hello, World!
"""
