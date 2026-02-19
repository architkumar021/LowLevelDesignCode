"""
Dependency — Document class in Python.

A Document depends on a Printer only during the print_document() call.
It does NOT store a reference to the Printer.
"""

from printer import Printer


class Document:
    """A document that can be printed using any Printer."""

    def __init__(self, title: str, content: str) -> None:
        self._title = title
        self._content = content

    @property
    def title(self) -> str:
        return self._title

    @property
    def content(self) -> str:
        return self._content

    def print_document(self, printer: Printer) -> None:
        """Dependency: Printer is passed in and used only here."""
        print(f"Document: {self._title}")
        printer.print_message(self._content)

    def __str__(self) -> str:
        return f"Document({self._title})"
