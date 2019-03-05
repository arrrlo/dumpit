import unittest

from dumpit.indent import Indent
from dumpit.analyse import Object
from dumpit.export import ToString


class TestAnalyse(unittest.TestCase):

    def setUp(self):
        class TestObject:
            foo = 'foo'
            bar = 'bar'

        self._object = TestObject()
        self._indent = Indent(depth=0)
        self._export = ToString(delimiter='')

        self.maxDiff = None

    def test_analyse(self):
        analyse = Object(self._object, self._indent, self._export)

        self.assertTrue(
            analyse.analyse()
                .endswith("bar: type: <class 'str'>foo: type: <class 'str'>"))
