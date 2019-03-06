import unittest

from dumpit.indent import Indent
from dumpit.export import ToString
from dumpit.analyse import Vertical
from dumpit.coloring import NoColors


class TestAnalyse(unittest.TestCase):

    def setUp(self):
        class TestObject:
            foo = 'foo'
            bar = 'bar'

        self._object = TestObject()
        self._indent = Indent(depth=0)
        self._export = ToString(delimiter='',
                                coloring=NoColors())

        self.maxDiff = None

    def test_analyse(self):
        analyse = Vertical(self._object, self._indent, self._export)

        self.assertTrue(
            analyse.analyse()
                .startswith("foo: type: <class 'str'>bar: type: <class 'str'>"))
