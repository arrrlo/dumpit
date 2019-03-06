import click
from typing import AnyStr
from abc import abstractmethod


class Coloring:
    """Coloring abstract class."""

    def __init__(self):
        pass

    @abstractmethod
    def style(self,
              string: AnyStr,
              fg: AnyStr = None,
              bg: AnyStr = None) -> AnyStr:
        """Color the string or not."""


class TerminalColors(Coloring):
    """Style text with terminal colors."""

    def style(self,
              string: AnyStr,
              fg: AnyStr = None,
              bg: AnyStr = None) -> AnyStr:
        """Color strings."""

        return click.style(string, fg=fg, bg=bg)


class NoColors(Coloring):
    """Don't style text."""

    def style(self,
              string: AnyStr,
              fg: AnyStr = None,
              bg: AnyStr = None) -> AnyStr:
        """No color strings."""

        return string


class NoColorsWithWarning(NoColors):
    """Same as Vertical but it prints warning message."""

    def __init__(self):
        click.secho('You have chosen unknown coloring. '
                    'Using NoColors instead.', fg='yellow')
        super().__init__()
