import unittest

from dumpit.indent import Indent


class TestIndent(unittest.TestCase):

    def setUp(self):
        self._indent_depth = 8
        self._indent_spaceholder = '-'

    def test_spaces(self):
        indent = Indent(depth=self._indent_depth,
                        spaceholder=self._indent_spaceholder)

        self.assertEqual(indent.spaces(), self._indent_spaceholder * 0)
        with indent:
            self.assertEqual(indent.spaces(), self._indent_spaceholder * self._indent_depth)
        self.assertEqual(indent.spaces(), self._indent_spaceholder * 0)
