from typing import Any, AnyStr

from dumpit.indent import Indent
from dumpit.analyse import Object
from dumpit.export import Print, ToString


def pdumpit(object_: Any) -> None:
    """Export object to standard output."""

    indent_ = Indent(depth=4)
    export_ = Print(delimiter='\n')

    Object(object_, indent_, export_).analyse()


def fdumpit(object_: Any) -> AnyStr:
    """Export object to string."""

    indent_ = Indent(depth=4)
    export_ = ToString(delimiter='\n')

    return Object(object_, indent_, export_).analyse()
