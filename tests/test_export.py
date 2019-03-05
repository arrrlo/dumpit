import unittest

from dumpit.export import ToString


class TestExport(unittest.TestCase):

    def setUp(self):
        self._delimiter = '\n'

    def test_export(self):
        export = ToString(delimiter=self._delimiter)

        export.store('foo')
        export.store('bar')

        self.assertEqual(export.export(), 'foo\nbar')
