import numpy as np

class trace:
    def __init__(self,value,_prev=(),_op="",_name=""):
        self.value = value
        self._prev = _prev
        self._op = _op
        self._name = _name
        self._id = id(self)
        if isinstance(value,np.ndarray):
            self.shape = value.shape
        else:
            self.shape = None

    def __repr__(self):
        return f"{self._name,self.value}"

    def __add__(self,other):
        return trace(self.value + other.value,(self,other),"+",f"{self._name}+{other._name}")

    def __mul__(self,other):
        return trace(self.value * other.value,(self,other),"*",f"{self._name}*{other._name}")

    def __getitem__(self,key):
        return trace(self.value[key],(self,),f"getitem",f"{self._name}[{key}]")

    def __len__(self):
        return len(self.value)

    def __radd__(self,other):
        return (other + self)

    def __rmul__(self,other):
        return (other * self)
