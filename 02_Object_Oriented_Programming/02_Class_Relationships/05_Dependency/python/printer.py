"""
Dependency — Printer class in Python.
"""


class Printer:
    """A printer that can print a message."""

    def __init__(self, printer_name: str) -> None:
        self._printer_name = printer_name

    @property
    def printer_name(self) -> str:
        return self._printer_name

    def print_message(self, message: str) -> None:
        print(f"[{self._printer_name}] Printing: {message}")

    def __str__(self) -> str:
        return f"Printer({self._printer_name})"
