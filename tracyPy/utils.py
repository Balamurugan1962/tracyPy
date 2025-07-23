from . import Var
import numpy as np

def sin(self):
    if not isinstance(self,Var):
        raise Exception("Invalid Type: sin() expects a Var object as its argument")

    newValue = np.sin(self.value)
    newName = f"SIN[{self.name}]"

    return Var(newValue,newName)

def sum(self,axis=0):
    if not isinstance(self,Var):
        raise Exception("Invalid Type: sin() expects a Var object as its argument")
    newValue = np.sum(self.value,axis=axis)
    newName = f"SUM[{self.name},{axis}]"
    return Var(newValue,newName)

def log2(self):
    if not isinstance(self,Var):
        raise Exception("Invalid Type: log2() expects a Var object as its argument")

    newValue = np.log2(self.value)
    newName = f"LOG2[{self.name}]"
    return Var(newValue,newName)
