from typing import Any, AnyStr

DESCRIPTIONS = {
    "__new__": "Initialization and Construction. \nTo get called in an object's instantiation.",
    "__init__": "Initialization and Construction. \nTo get called by the __new__ method.",
    "__del__": "Initialization and Construction. \nDestructor method.",

    "__pos__": "Unary operators and functions. \nTo get called for unary positive e.g. \n+someobject.",
    "__neg__": "Unary operators and functions. \nTo get called for unary negative e.g. \n-someobject.",
    "__abs__": "Unary operators and functions. \nTo get called by built-in abs() function.",
    "__invert__": "Unary operators and functions. \nTo get called for inversion using \nthe ~ operator.",
    "__round__": "Unary operators and functions. \nTo get called by built-in round() \nfunction.",
    "__floor__": "Unary operators and functions. \nTo get called by built-in math.floor()\n function.",
    "__ceil__": "Unary operators and functions. \nTo get called by built-in math.ceil() \nfunction.",
    "__trunc__": "Unary operators and functions. \nTo get called by built-in math.trunc() \nfunction.",

    "__iadd__": "Augmented Assignment. \nTo get called on addition with \nassignment e.g. a +=b.",
    "__isub__": "Augmented Assignment. \nTo get called on subtraction with \nassignment e.g. a -=b.",
    "__imul__": "Augmented Assignment. \nTo get called on multiplication with \nassignment e.g. a *=b.",
    "__ifloordiv__": "Augmented Assignment. \nTo get called on integer division \nwith assignment e.g. a //=b.",
    "__idiv__": "Augmented Assignment. \nTo get called on division with \nassignment e.g. a /=b.",
    "__itruediv__": "Augmented Assignment. \nTo get called on true division \nwith assignment",
    "__imod__": "Augmented Assignment. \nTo get called on modulo with \nassignment e.g. a%=b.",
    "__ipow__": "Augmented Assignment. \nTo get called on exponentswith \nassignment e.g. a **=b.",
    "__ilshift__": "Augmented Assignment. \nTo get called on left bitwise \nshift with assignment e.g. a<<=b.",
    "__irshift__": "Augmented Assignment. \nTo get called on right bitwise \nshift with assignment e.g. a >>=b.",
    "__iand__": "Augmented Assignment. \nTo get called on bitwise AND with \nassignment e.g. a&=b.",
    "__ior__": "Augmented Assignment. \nTo get called on bitwise OR with \nassignment e.g. a|=b.",
    "__ixor__": "Augmented Assignment. \nTo get called on bitwise XOR with \nassignment e.g. a ^=b.",

    "__int__": "Type Conversion Dunder (Magic) Methods. \nTo get called by built-int int() method \nto convert a type to an int.",
    "__float__": "Type Conversion Dunder (Magic) Methods. \nTo get called by built-int float() \nmethod to convert a type to float.",
    "__complex__": "Type Conversion Dunder (Magic) Methods. \nTo get called by built-int complex() \nmethod to convert a type to complex.",
    "__oct__": "Type Conversion Dunder (Magic) Methods. \nTo get called by built-int oct() method \nto convert a type to octal.",
    "__hex__": "Type Conversion Dunder (Magic) Methods. \nTo get called by built-int hex() method \nto convert a type to hexadecimal.",
    "__index__": "Type Conversion Dunder (Magic) Methods. \nTo get called on type conversion to an \nint when the object is used in a slice expression.",

    "__str__": "String Dunder (Magic) Methods. \nTo get called by built-int str() method \nto return a string representation of a type.",
    "__repr__": "String Dunder (Magic) Methods. \nTo get called by built-int repr() method \nto return a machine readable representation of a type.",
    "__unicode__": "String Dunder (Magic) Methods. \nTo get called by built-int unicode() \nmethod to return an unicode string of a type.",
    "__format__": "String Dunder (Magic) Methods. \nTo get called by built-int string.format() \nmethod to return a new style of string.",
    "__hash__": "String Dunder (Magic) Methods. \nTo get called by built-int hash() method \nto return an integer.",
    "__nonzero__": "String Dunder (Magic) Methods. \nTo get called by built-int bool() \nmethod to return True or False.",
    "__dir__": "String Dunder (Magic) Methods. \nTo get called by built-int dir() method \nto return a list of attributes of a class.",
    "__sizeof__": "String Dunder (Magic) Methods. \nTo get called by built-int sys.getsizeof() \nmethod to return the size of an object.",

    "__getattr__": "Attribute Dunder (Magic) Methods. \nIs called when the accessing attribute \nof a class that does not exist.",
    "__setattr__": "Attribute Dunder (Magic) Methods. \nIs called when assigning a value to \nthe attribute of a class.",
    "__delattr__": "Attribute Dunder (Magic) Methods. \nIs called when deleting an attribute \nof a class.",

    "__add__": "Operator Dunder (Magic) Methods. \nTo get called on add operation using + \noperator.",
    "__sub__": "Operator Dunder (Magic) Methods. \nTo get called on subtraction operation \nusing - operator.",
    "__mul__": "Operator Dunder (Magic) Methods. \nTo get called on multiplication operation \nusing * operator.",
    "__floordiv__": "Operator Dunder (Magic) Methods. \nTo get called on floor division \noperation using // operator.",
    "__div__": "Operator Dunder (Magic) Methods. \nTo get called on division operation \nusing / operator.",
    "__mod__": "Operator Dunder (Magic) Methods. \nTo get called on modulo operation \nusing % operator.",
    "__pow__": "Operator Dunder (Magic) Methods. \nTo get called on calculating the \npower using ** operator.",
    "__lt__": "Operator Dunder (Magic) Methods. \nTo get called on comparison using \n< operator.",
    "__le__": "Operator Dunder (Magic) Methods. \nTo get called on comparison using \n<= operator.",
    "__eq__": "Operator Dunder (Magic) Methods. \nTo get called on comparison using \n== operator.",
    "__ne__": "Operator Dunder (Magic) Methods. \nTo get called on comparison using \n!= operator.",
    "__ge__": "Operator Dunder (Magic) Methods. \nTo get called on comparison using \n>= operator.",

    "__doc__": "A short documentation which describes the features.",
    "__class__": "The class to which a class instance belongs.",
    "__contains__": "Called to implement membership test operators.",
    "__getitem__": "Called to implement evaluation of self[key].",
    "__gt__": "Called to implement x>y.",
    "__init_subclass__": "This method is called whenever the \ncontaining class is subclassed.",
    "__iter__": "This method is called when an iterator is required \nfor a container.",
    "__len__": "Called to implement the built-in function len().",
    "__reduce__": "",
    "__reduce_ex__": "",
    "__setitem__": "Called to implement assignment to self[key].",
    "__subclasshook__": "",
    "__delitem__": "Called to implement deletion of self[key].",
    "__getattribute__": "Called unconditionally to implement \nattribute accesses for instances of the class.",
    "__bool__": "Called to implement truth value testing and the \nbuilt-in operation bool(); should return False or True."
}


def get_description(attribute: Any, name: AnyStr,
                    indent: AnyStr = '') -> AnyStr:
    """Get objects attribute description."""

    desc = DESCRIPTIONS.get(name, '')

    if not desc:
        try:
            desc = attribute.__doc__ or ''
        except AttributeError:
            desc = ''

    if desc:
        desc = desc.replace('\n', f'\n{indent}')

    return desc
