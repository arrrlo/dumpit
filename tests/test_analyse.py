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

        self.assertEqual(analyse.analyse(), "__class__: type: <class 'type'>__delattr__: type: <class 'method-wrapper'>args: ['name']__dict__: type: <class 'dict'>__dir__: type: <class 'builtin_function_or_method'>__doc__: type: <class 'NoneType'>__eq__: type: <class 'method-wrapper'>args: ['value']__format__: type: <class 'builtin_function_or_method'>args: ['format_spec']__ge__: type: <class 'method-wrapper'>args: ['value']__getattribute__: type: <class 'method-wrapper'>args: ['name']__gt__: type: <class 'method-wrapper'>args: ['value']__hash__: type: <class 'method-wrapper'>__init__: type: <class 'method-wrapper'>args: ['*args', '**kwargs']__init_subclass__: type: <class 'builtin_function_or_method'>__le__: type: <class 'method-wrapper'>args: ['value']__lt__: type: <class 'method-wrapper'>args: ['value']__module__: type: <class 'str'>__ne__: type: <class 'method-wrapper'>args: ['value']__new__: type: <class 'builtin_function_or_method'>args: ['*args', '**kwargs']__reduce__: type: <class 'builtin_function_or_method'>__reduce_ex__: type: <class 'builtin_function_or_method'>args: ['protocol']__repr__: type: <class 'method-wrapper'>__setattr__: type: <class 'method-wrapper'>args: ['name', 'value']__sizeof__: type: <class 'builtin_function_or_method'>__str__: type: <class 'method-wrapper'>__subclasshook__: type: <class 'builtin_function_or_method'>__weakref__: type: <class 'NoneType'>bar: type: <class 'str'>foo: type: <class 'str'>")
