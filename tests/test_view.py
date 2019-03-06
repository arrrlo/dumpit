import unittest

from dumpit.view import Vertical
from dumpit.indent import Indent
from dumpit.export import ToString
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

    def test_run(self):
        view = Vertical(self._object, self._indent, self._export)

        self.assertTrue(
            view.run()
                .startswith("foo: type: <class 'str'>bar: type: <class 'str'>"))
