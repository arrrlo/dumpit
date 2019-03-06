from typing import Any, AnyStr, Union

from dumpit.indent import Indent
from dumpit.analyse import Vertical
from dumpit.export import Print, ToString
from dumpit.coloring import TerminalColors, NoColors, Coloring


def coloring_object(colors: AnyStr) -> 'Coloring':
    """Choose which coloring object."""

    return {
       'terminal': TerminalColors,

    }.get(colors, NoColors)()


def pdumpit(object_: Any,
            colors: Union[bool, str] = 'terminal') -> None:
    """Export object to standard output."""

    indent_ = Indent(depth=4)
    export_ = Print(delimiter='\n',
                    coloring=coloring_object(colors))

    Vertical(object_, indent_, export_).analyse()


def fdumpit(object_: Any,
            colors: Union[bool, str] = False) -> AnyStr:
    """Export object to string."""

    indent_ = Indent(depth=4)
    export_ = ToString(delimiter='\n',
                       coloring=coloring_object(colors))

    return Vertical(object_, indent_, export_).analyse()
