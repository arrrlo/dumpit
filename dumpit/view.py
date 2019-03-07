import click
from inspect import signature
from abc import abstractmethod
from typing import Any, AnyStr, List
from terminaltables import AsciiTable

from dumpit.indent import Indent
from dumpit.export import Export
from dumpit.description import get_description


class View:
    """View abstract class."""

    def __init__(self, data: Any, indent: 'Indent',
                 export: 'Export', show_dunders: bool = True):
        self._data = data
        self._indent = indent
        self._export = export
        self._show_dunders = show_dunders

    @abstractmethod
    def run(self):
        """Do the abstract run."""

    def _type_color(self, attr_name: AnyStr) -> AnyStr:
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

    def _is_dunder(self, attr_name: AnyStr) -> bool:
        """Check if the attribute is a dunder method (magic method)."""

        return attr_name.startswith('__') and attr_name.endswith('__')
    
    def _arguments(self, attribute: Any) -> List:
        """Get attributes of a method."""

        try:
            sig = signature(attribute)
            attrs = dict(sig.parameters)

        except ValueError:
            attrs = None
        except TypeError:
            attrs = None

        if attrs:
            return [str(attr) for attr in dict(attrs).values()]
        else:
            return []


class Vertical(View):
    """Vertical view class."""

    def run(self) -> AnyStr:
        """Do the run."""

        for value in reversed(dir(self._data)):

            # don't show dunders if marked by _show_dunders
            if self._is_dunder(value) and not self._show_dunders:
                continue

            attribute = getattr(self._data, value)

            # store objects attribute name
            self._export.store(f'{value}: ', fg=self._type_color(value))

            # second indentation
            with self._indent as indent:

                # store objects attribute type
                self._export.store(
                    f'{indent()}type: {str(type(attribute))}',
                    fg='blue', bold=True
                )

                attrs_list = self._arguments(attribute)

                # store objects method arguments
                if attrs_list:
                    self._export.store(
                        f'{indent()}args: {str(", ".join(attrs_list))}')

                # get attribute description with indentation
                desc = get_description(attribute, value,
                                       indent=f'{indent()}      ')
                if desc:
                    # store attribute description
                    self._export.store(
                        f'{indent()}desc: {desc}')

                self._export.store(indent())

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

            # don't show dunders if marked by _show_dunders
            if self._is_dunder(value) and not self._show_dunders:
                continue

            attribute = getattr(self._data, value)

            data.append(
                [
                    click.style(value, fg=self._type_color(value)),
                    click.style(str(type(attribute)), fg='blue', bold=True),
                    '\n'.join(self._arguments(attribute)).replace(', ', '\n'),
                    get_description(attribute, value)
                ]
            )

        header = ['name', 'type', 'arguments', 'description']
        table = AsciiTable([header] + data)
        table.inner_row_border = True

        # save the table
        self._export.store(table.table)

        # print to standard output or return
        return self._export.export()
