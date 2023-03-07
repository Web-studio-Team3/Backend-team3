class ValueObjects(object):

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__hash__()})'

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __ne__(self, other):
        return repr(self) != repr(other)
