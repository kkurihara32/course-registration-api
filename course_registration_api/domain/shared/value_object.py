class ValueObject(object):
    def __init__(self, value=None):
        self._value = value

    def __eq__(self, other):
        if other is None or not isinstance(other, ValueObject):
            return False
        else:
            return self.value == other.value

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    @property
    def value(self):
        return self._value
