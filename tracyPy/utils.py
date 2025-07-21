from . import Var
import numpy as np

def sin(self):
    if not isinstance(self,Var):
        raise Exception("sin() expects a Var object as its argument")

    newValue = np.sin(self.value)
    newName = f"sin[{self.name}]"

    return Var(newValue,newName)
