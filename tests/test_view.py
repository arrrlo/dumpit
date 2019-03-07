import os
import unittest

from dumpit.indent import Indent
from dumpit.export import ToString
from dumpit.coloring import NoColors
from dumpit.view import Vertical, Table


class TestView(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

        class TestObject:
            foo = None

        _object = TestObject()
        _indent = Indent(depth=0, spaceholder='')
        _export = ToString(delimiter='',
                           coloring=NoColors())

        self._vertical_view = Vertical(_object, _indent, _export,
                                       show_dunders=False)
        self._table_view = Table(_object, _indent, _export,
                                 show_dunders=False)

        _base_dir = os.path.join(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            ), 'tests'
        )

        self._vertical_view_file = os.path.join(_base_dir, 'vertical_view.txt')
        self._table_view_file = os.path.join(_base_dir, 'table_view.txt')

    def test_vertical(self):
        output = self._vertical_view.run()

        with open(self._vertical_view_file) as f:
            self.assertEqual(output, f.read())

    def test_table(self):
        output = self._table_view.run()

        with open(self._table_view_file) as f:
            self.assertEqual(output, f.read())
