import click
from abc import abstractmethod
from typing import Any, AnyStr, List

from dumpit.coloring import Coloring


class Export:
    """Export abstract class."""

    def __init__(self, delimiter: AnyStr,
                 coloring: 'Coloring'):
        self._exported = list()
        self._delimiter = delimiter
        self._coloring = coloring

    @abstractmethod
    def export(self, *args, **kwargs) -> Any:
        """Do the abstract export."""

    def store(self,
              text: AnyStr,
              fg: AnyStr = None,
              bg: AnyStr = None) -> None:
        """Store text in export object."""

        text = self._coloring.style(text, fg=fg, bg=bg)
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
