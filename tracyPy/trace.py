class trace:
    def __init__(self,value,_prev=(),_op="",_name=""):
        self.value = value
        self._prev = _prev
        self._op = _op
        self._name = _name

    def __repr__(self):
        return f"{self._name}"

    def __add__(self,other):
        return trace(self.value + other.value,(self,other),"+",f"{self._name}+{other._name}")

    def __radd__(self,other):
        return (other + self)
