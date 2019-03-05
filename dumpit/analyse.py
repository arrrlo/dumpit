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


class Object(Analyse):
    """Object analyse class."""

    def analyse(self) -> AnyStr:
        """Do the analyse."""

        with self._indent:
            for value in dir(self._data):

                self._export.store(
                    self._indent.spaces() + value + ': ')
                attribute = getattr(self._data, value)

                with self._indent:
                    self._export.store(
                        self._indent.spaces() +
                        'type: ' + str(type(attribute)))

                    try:
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
                            self._export.store(
                                self._indent.spaces() +
                                'args: ' + str(attrs_list))

                    self._export.store(self._indent.spaces())

        return self._export.export()
