import click
from inspect import signature
from abc import abstractmethod
from typing import Any, AnyStr, List
from terminaltables import AsciiTable

from dumpit.indent import Indent
from dumpit.export import Export


class View:
    """View abstract class."""

    def __init__(self, data: Any, indent: 'Indent',
                 export: 'Export'):
        self._data = data
        self._indent = indent
        self._export = export

    @abstractmethod
    def run(self):
        """Do the abstract run."""

    def _type_color(self, attr_name: AnyStr):
        """Choose color for objects attribute."""

        if attr_name.startswith('__') and \
           attr_name.endswith('__'):
            return 'red'
        if attr_name.startswith('__') and \
           not attr_name.endswith('__'):
            return 'yellow'
        if attr_name.startswith('_') and \
           not attr_name.startswith('__'):
            return 'yellow'
        else:
            return 'green'
    
    def _arguments(self, attribute) -> List:
        """Get attributes of a method."""

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
                return [str(attr) for attr in
                              dict(attrs).values()]
            else:
                return []


class Vertical(View):
    """Vertical view class."""

    def run(self) -> AnyStr:
        """Do the run."""

        # first indentation
        with self._indent:
            for value in reversed(dir(self._data)):

                attribute = getattr(self._data, value)

                # store objects attribute name
                self._export.store(
                    self._indent.spaces() + value + ': ',
                    fg=self._type_color(value)
                )

                # second indentation
                with self._indent:

                    # store objects attribute type
                    self._export.store(
                        self._indent.spaces() +
                        'type: ' + str(type(attribute)))

                    attrs_list = self._arguments(attribute)

                    # store objects method arguments
                    if attrs_list:
                        args = 'args: ' + str(', '.join(attrs_list))
                    else:
                        args = ''
                    self._export.store(
                        self._indent.spaces() + args)

                    self._export.store(self._indent.spaces())

        # print to standard output or return
        return self._export.export()


class VerticalWithWarning(Vertical):
    """Same as Vertical but it prints warning message."""

    def __init__(self, *args, **kwargs):
        click.secho('You have chosen unknown view. '
                    'Using Vertical instead.', fg='yellow')
        super().__init__(*args, **kwargs)


class Table(View):
    """Vertical view class."""

    def run(self) -> AnyStr:
        """Do the run."""

        data = []
        for value in reversed(dir(self._data)):
            attribute = getattr(self._data, value)

            attrs_list = self._arguments(attribute)

            # store objects attribute name
            data.append(
                [click.style(value, fg=self._type_color(value)),
                 str(type(attribute)),
                 '\n'.join(attrs_list)]
            )

        header = ['name', 'type', 'arguments']
        table = AsciiTable([header] + data)
        table.inner_row_border = True
        table.inner_heading_row_border = False

        # save the table
        self._export.store(table.table)

        # print to standard output or return
        return self._export.export()
