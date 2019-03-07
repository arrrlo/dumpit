from typing import Any, AnyStr, Union, Type

from dumpit.indent import Indent
from dumpit.export import Print, ToString
from dumpit.view import (Vertical, Table,
                         VerticalWithWarning)
from dumpit.coloring import (TerminalColors, NoColors,
                             NoColorsWithWarning)


ViewsType = Type[Union[Vertical, Table, VerticalWithWarning]]
ColoringType = Union[TerminalColors, NoColors, NoColorsWithWarning]


def __view_class(view: AnyStr) -> ViewsType:
    """Choose which coloring object."""

    return {
        'vertical': Vertical,
        'table': Table,

    }.get(view, VerticalWithWarning)


def __coloring_object(colors: AnyStr) -> ColoringType:
    """Choose which coloring object."""

    return {
        'terminal': TerminalColors,
        False: NoColors

    }.get(colors, NoColorsWithWarning)()


def pdumpit(object_: Any,
            view_: AnyStr = 'table',
            colors: Union[bool, str] = 'terminal',
            all_: bool = True) -> None:
    """
    Export object to standard output.

    :param object_: Any kind of python object.
    :param view_: Choose between Vertical or Table view
    :param colors: Should attribute names be in colors or not.
    :param all_: Show all attributes Otherwise dunder methods are excluded.
    :return: None
    """

    indent_ = Indent(depth=4)
    export_ = Print(delimiter='\n',
                    coloring=__coloring_object(colors))

    __view_class(view_)(object_, indent_, export_,
                        show_dunders=all_).run()


def fdumpit(object_: Any,
            view_: AnyStr = 'vertical',
            colors: Union[bool, str] = False,
            all_: bool = True) -> AnyStr:
    """
    Export object to string.

    :param object_: Any kind of python object.
    :param view_: Choose between Vertical or Table view
    :param colors: Should attribute names be in colors or not.
    :param all_: Show all attributes Otherwise dunder methods are excluded.
    :return:
    """

    indent_ = Indent(depth=4)
    export_ = ToString(delimiter='\n',
                       coloring=__coloring_object(colors))

    return __view_class(view_)(object_, indent_, export_,
                               show_dunders=all_).run()
