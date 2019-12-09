# read_only_properties is also available as pip package
def read_only_properties(*attrs):
    def class_rebuilder(cls):
        "The class decorator"
        class NewClass(cls):
            "This is the overwritten class"
            def __setattr__(self, name, value):
                if name not in attrs:
                    pass
                elif name not in self.__dict__:
                    pass
                else:
                    raise AttributeError("Can't modify {}".format(name))

                super().__setattr__(name, value)
        return NewClass
    return class_rebuilder


@read_only_properties('nothing')
class Maybe(object):
    """The Maybe Monad"""
    def __init__(self, value):
        self._value = value
        self.nothing = "Nothing"

    def __str__(self):
        if self._value is not None:
            return f"Just {self._value}"
        else:
            return self.nothing

    @staticmethod
    def return_maybe(value):
        """The monad return operator"""
        """a -> m a"""
        if value is not None:
            return Maybe(value)
        else:
            raise Exception("Illegal Operation")

    def bind(self, func):
        """The monad bind (>>=) operator"""
        """m a -> (a -> m b) -> m b"""
        if callable(func) and self._value is not None:
            return func(self._value)
        else:
            return Maybe(None)

    def just_value(self):
        """Returns the underlying value"""
        if self._value is not None:
            return self._value
        else:
            raise Exception("Illegal Operation, No Just value")


@read_only_properties('_left')
class Either(object):
    """The Either Monad"""
    def __init__(self, value, error: str = "no valid value"):
        self._right = value
        self._left = error

    def __str__(self):
        if self._right is not None:
            return f"Right {self._right}"
        else:
            raise Exception(self._left)

    @staticmethod
    def return_either(value):
        """The monad return operator"""
        """a -> m a"""
        if value is not None:
            return Either(value)
        else:
            raise Exception("Illegal Operation")

    def bind(self, func):
        """The monad bind (>>=) operator"""
        """m a -> (a -> m b) -> m b"""
        if callable(func) and self._right is not None:
            return func(self._right)
        else:
            raise Exception(self._left)

    def right_value(self):
        """Returns the underlying value"""
        if self._right is not None:
            return self._right
        else:
            raise Exception("Illegal Operation, No right value")