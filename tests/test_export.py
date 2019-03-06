import unittest

from dumpit.export import ToString
from dumpit.coloring import NoColors


class TestExport(unittest.TestCase):

    def setUp(self):
        self._delimiter = '\n'

    def test_export(self):
        export = ToString(delimiter=self._delimiter,
                          coloring=NoColors())

        export.store('foo')
        export.store('bar')

        self.assertEqual(export.export(), 'foo\nbar')
