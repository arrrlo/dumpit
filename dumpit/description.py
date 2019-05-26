from typing import Any, AnyStr

DESCRIPTIONS = {
    "__new__": "Initialization and Construction. \n"
               "To get called in an object's instantiation.",

    "__init__": "Initialization and Construction. \n"
                "To get called by the __new__ method.",

    "__del__": "Initialization and Construction. \n"
               "Destructor method.",

    "__pos__": "Unary operators and functions. \n"
               "To get called for unary positive e.g. \n"
               "+someobject.",

    "__neg__": "Unary operators and functions. \n"
               "To get called for unary negative e.g. \n"
               "-someobject.",

    "__abs__": "Unary operators and functions. \n"
               "To get called by built-in abs() function.",

    "__invert__": "Unary operators and functions. \n"
                  "To get called for inversion using \n"
                  "the ~ operator.",

    "__round__": "Unary operators and functions. \n"
                 "To get called by built-in round() \n"
                 "function.",

    "__floor__": "Unary operators and functions. \n"
                 "To get called by built-in math.floor()\n"
                 " function.",

    "__ceil__": "Unary operators and functions. \n"
                "To get called by built-in math.ceil() \n"
                "function.",

    "__trunc__": "Unary operators and functions. \n"
                 "To get called by built-in math.trunc() \n"
                 "function.",

    "__iadd__": "Augmented Assignment. \n"
                "To get called on addition with \n"
                "assignment e.g. a +=b.",

    "__isub__": "Augmented Assignment. \n"
                "To get called on subtraction with \n"
                "assignment e.g. a -=b.",

    "__imul__": "Augmented Assignment. \n"
                "To get called on multiplication with \n"
                "assignment e.g. a *=b.",

    "__ifloordiv__": "Augmented Assignment. \n"
                     "To get called on integer division \n"
                     "with assignment e.g. a //=b.",

    "__idiv__": "Augmented Assignment. \n"
                "To get called on division with \n"
                "assignment e.g. a /=b.",

    "__itruediv__": "Augmented Assignment. \n"
                    "To get called on true division \n"
                    "with assignment",

    "__imod__": "Augmented Assignment. \n"
                "To get called on modulo with \n"
                "assignment e.g. a%=b.",

    "__ipow__": "Augmented Assignment. \n"
                "To get called on exponentswith \n"
                "assignment e.g. a **=b.",

    "__ilshift__": "Augmented Assignment. \n"
                   "To get called on left bitwise \n"
                   "shift with assignment e.g. a<<=b.",

    "__irshift__": "Augmented Assignment. \n"
                   "To get called on right bitwise \n"
                   "shift with assignment e.g. a >>=b.",

    "__iand__": "Augmented Assignment. \n"
                "To get called on bitwise AND with \n"
                "assignment e.g. a&=b.",

    "__ior__": "Augmented Assignment. \n"
               "To get called on bitwise OR with \n"
               "assignment e.g. a|=b.",

    "__ixor__": "Augmented Assignment. \n"
                "To get called on bitwise XOR with \n"
                "assignment e.g. a ^=b.",

    "__int__": "Type Conversion Dunder (Magic) Methods. \n"
               "To get called by built-int int() method \n"
               "to convert a type to an int.",

    "__float__": "Type Conversion Dunder (Magic) Methods. \n"
                 "To get called by built-int float() \n"
                 "method to convert a type to float.",

    "__complex__": "Type Conversion Dunder (Magic) Methods. \n"
                   "To get called by built-int complex() \n"
                   "method to convert a type to complex.",

    "__oct__": "Type Conversion Dunder (Magic) Methods. \n"
               "To get called by built-int oct() method \n"
               "to convert a type to octal.",

    "__hex__": "Type Conversion Dunder (Magic) Methods. \n"
               "To get called by built-int hex() method \n"
               "to convert a type to hexadecimal.",

    "__index__": "Type Conversion Dunder (Magic) Methods. \n"
                 "To get called on type conversion to an \n"
                 "int when the object is used in a slice expression.",

    "__str__": "String Dunder (Magic) Methods. \n"
               "To get called by built-int str() method \n"
               "to return a string representation of a type.",

    "__repr__": "String Dunder (Magic) Methods. \n"
                "To get called by built-int repr() method \n"
                "to return a machine readable representation of a type.",

    "__unicode__": "String Dunder (Magic) Methods. \n"
                   "To get called by built-int unicode() \n"
                   "method to return an unicode string of a type.",

    "__format__": "String Dunder (Magic) Methods. \n"
                  "To get called by built-int string.format() \n"
                  "method to return a new style of string.",

    "__hash__": "String Dunder (Magic) Methods. \n"
                "To get called by built-int hash() method \n"
                "to return an integer.",

    "__nonzero__": "String Dunder (Magic) Methods. \n"
                   "To get called by built-int bool() \n"
                   "method to return True or False.",

    "__dir__": "String Dunder (Magic) Methods. \n"
               "To get called by built-int dir() method \n"
               "to return a list of attributes of a class.",

    "__sizeof__": "String Dunder (Magic) Methods. \n"
                  "To get called by built-int sys.getsizeof() \n"
                  "method to return the size of an object.",

    "__getattr__": "Attribute Dunder (Magic) Methods. \n"
                   "Is called when the accessing attribute \n"
                   "of a class that does not exist.",

    "__setattr__": "Attribute Dunder (Magic) Methods. \n"
                   "Is called when assigning a value to \n"
                   "the attribute of a class.",

    "__delattr__": "Attribute Dunder (Magic) Methods. \n"
                   "Is called when deleting an attribute \n"
                   "of a class.",

    "__add__": "Operator Dunder (Magic) Methods. \n"
               "To get called on add operation using + \n"
               "operator.",

    "__sub__": "Operator Dunder (Magic) Methods. \n"
               "To get called on subtraction operation \n"
               "using - operator.",

    "__mul__": "Operator Dunder (Magic) Methods. \n"
               "To get called on multiplication operation \n"
               "using * operator.",

    "__floordiv__": "Operator Dunder (Magic) Methods. \n"
                    "To get called on floor division \n"
                    "operation using // operator.",

    "__div__": "Operator Dunder (Magic) Methods. \n"
               "To get called on division operation \n"
               "using / operator.",

    "__mod__": "Operator Dunder (Magic) Methods. \n"
               "To get called on modulo operation \n"
               "using % operator.",

    "__pow__": "Operator Dunder (Magic) Methods. \n"
               "To get called on calculating the \n"
               "power using ** operator.",

    "__lt__": "Operator Dunder (Magic) Methods. \n"
              "To get called on comparison using \n"
              "< operator.",

    "__le__": "Operator Dunder (Magic) Methods. \n"
              "To get called on comparison using \n"
              "<= operator.",

    "__eq__": "Operator Dunder (Magic) Methods. \n"
              "To get called on comparison using \n"
              "== operator.",

    "__ne__": "Operator Dunder (Magic) Methods. \n"
              "To get called on comparison using \n"
              "!= operator.",

    "__ge__": "Operator Dunder (Magic) Methods. \n"
              "To get called on comparison using \n"
              ">= operator.",

    "__doc__": "A short documentation which describes the features.",

    "__class__": "The class to which a class instance belongs.",

    "__contains__": "Called to implement membership test operators.",

    "__getitem__": "Called to implement evaluation of self[key].",

    "__gt__": "Called to implement x>y.",

    "__init_subclass__": "This method is called whenever the \n"
                         "containing class is subclassed.",

    "__iter__": "This method is called when an iterator is required \n"
                "for a container.",

    "__len__": "Called to implement the built-in function len().",

    "__reduce__": "",

    "__reduce_ex__": "",

    "__setitem__": "Called to implement assignment to self[key].",

    "__subclasshook__": "",

    "__delitem__": "Called to implement deletion of self[key].",

    "__getattribute__": "Called unconditionally to implement \n"
                        "attribute accesses for instances of the class.",

    "__bool__": "Called to implement truth value testing and the \n"
                "built-in operation bool(); should return False or True."
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
        desc = desc.replace('\n', '\n{}'.format(indent))

    return desc
