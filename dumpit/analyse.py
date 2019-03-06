from inspect import signature
from abc import abstractmethod
from typing import Any, AnyStr

from dumpit.indent import Indent
from dumpit.export import Export


class Analyse:
    """Analyse abstract class."""

    def __init__(self, data: Any, indent: 'Indent',
                 export: 'Export'):
        self._data = data
        self._indent = indent
        self._export = export

    @abstractmethod
    def analyse(self):
        """Do the abstract analyse."""

    def type_color(self, attr_name: AnyStr):
        """Choose color for objects attribute."""

        if attr_name.startswith('__') and \
           attr_name.endswith('__'):
            return 'red'
        if attr_name.startswith('_') and \
           not attr_name.startswith('__'):
            return 'yellow'
        else:
            return 'green'


class Vertical(Analyse):
    """Vertical analyse class."""

    def analyse(self) -> AnyStr:
        """Do the analyse."""

        # first indentation
        with self._indent:
            for value in reversed(dir(self._data)):

                attribute = getattr(self._data, value)

                # store objects attribute name
                self._export.store(
                    self._indent.spaces() + value + ': ',
                    fg=self.type_color(value)
                )

                # second indentation
                with self._indent:

                    # store objects attribute type
                    self._export.store(
                        self._indent.spaces() +
                        'type: ' + str(type(attribute)))

                    try:
                        # get methods arguments
                        sig = signature(attribute)
                        attrs = dict(sig.parameters)

                    except ValueError:
                        attrs = None
                    except TypeError:
                        attrs = None

                    finally:
                        if attrs:
                            attrs_list = [str(attr) for attr in
                                          dict(attrs).values()]

                            # store objects method arguments
                            self._export.store(
                                self._indent.spaces() +
                                'args: ' + str(attrs_list))

                    self._export.store(self._indent.spaces())

        # print to standard output or return
        return self._export.export()
