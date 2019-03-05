import click
from typing import Any, AnyStr
from abc import abstractmethod


class Export:
    """Export abstract class."""

    def __init__(self, delimiter: AnyStr):
        self._exported = list()
        self._delimiter = delimiter

    @abstractmethod
    def export(self) -> Any:
        """Do the abstract export."""

    def store(self, text: AnyStr) -> None:
        """Store text in export object."""

        self._exported.append(text)


class Print(Export):
    """Export by printing to standard output."""

    def export(self) -> None:
        """Do the export."""

        click.echo(self._delimiter.join(self._exported))


class ToString(Export):
    """Export by storing into class variable
    in textual format."""

    def export(self) -> AnyStr:
        """Do the export."""

        return self._delimiter.join(self._exported)
