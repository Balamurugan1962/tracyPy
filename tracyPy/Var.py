import numpy as np

class Var:
    primitives = (bool, int, float)

    def __init__(self,value,name):
        self.value = value
        self.name = name
        self.data = value

    def __repr__(self):
        return self.name + " = " + str(self.data)

    def __radd__(self,other):
        return self.__add__(other)

    def __rsub__(self,other):
        return self.__sub__(other)

    def __rmul__(self,other):
        return self.__mul__(other)

    def __rtruediv__(self,other):
        return self.__truediv__(other)


    def __add__(self,other):

        if isinstance(other,Var):
            newValue = self.value + other.value
            newName = f"({self.name} + {other.name})"
        elif isinstance(other,self.primitives):
            newValue = self.value + other
            newName = f"({self.name} + {other})"
        else:
            raise Exception("Invalid Type; Operation is only done with Var,bool, int and float types")

        return Var(newValue,newName)


    def __sub__(self,other):
        if isinstance(other,Var):
            newValue = self.value - other.value
            newName = f"({self.name} - {other.name})"
        elif isinstance(other,self.primitives):
            newValue = self.value - other
            newName = f"({self.name} - {other})"
        else:
            raise Exception("Invalid Type; Operation is only done with Var,bool, int and float types")

        return Var(newValue,newName)

    def __mul__(self,other):
        if isinstance(other,Var):
            newValue = self.value * other.value
            newName = f"({self.name} * {other.name})"
        elif isinstance(other,self.primitives):
            newValue = self.value * other
            newName = f"({self.name} * {other})"
        else:
            raise Exception("Invalid Type; Operation is only done with Var,bool, int and float types")

        return Var(newValue,newName)

    def __truediv__(self,other):
        if isinstance(other,Var):
            newValue = self.value / other.value
            newName = f"({self.name} / {other.name})"
        elif isinstance(other,self.primitives):
            newValue = self.value / other
            newName = f"({self.name} / {other})"
        else:
            raise Exception("Invalid Type; Operation is only done with Var,bool, int and float types")

        return Var(newValue,newName)








    def __getitem__(self, idx):

        if isinstance(idx,tuple):
            idxstr = ""
            for i in idx:
                if isinstance(i,slice):
                    idxstr +=":,"
                else:
                    idxstr += str(i)

        else:
            idxstr = str(idx)

        if isinstance(idx,Var):
            newValue =  self.data[idx.value]
            newName = f"{self.name}[{idx.name}]"
        else:
            newValue = self.data[idx]
            newName = f"{self.name}[{idxstr}]"

        return Var(newValue,newName)

    def __setitem__(self, idx, value):
        self.data[idx] = value






    def __eq__(self, other):
        if isinstance(other,Var):
            newValue = (self.value == other.value)
            newName = f"[{self.name}=={other.name}]"

        elif isinstance(other,self.primitives):
            newValue = (self.value == other)
            newName = f"[{self.name}=={other}]"
        else:
            raise Exception("Invalid Type: Operation is only done with Var,bool, int and float types")

        return Var(newValue,newName)


    def __pow__(self,other):
        if isinstance(other,Var):
            newValue = self.value ** other.value
            newName = f"({self.name} ** {other.name})"
        elif isinstance(other,int):
            newValue = self.value ** other
            newName = f"({self.name} ** {other})"
        else:
            raise Exception("Invalid Type; Operation is only done with Var,bool, int and float types")

        return Var(newValue,newName)






    def dot(self,other):
        if not isinstance(other,Var):
            raise Exception("Invalid Type: Expected only Var type")

        newValue = self.value.dot(other.value)
        newName = f"({self.name}.{other.name})"

        return Var(newValue,newName)

    def T(self):
        newValue = self.value.T
        newName = f"({self.name}.T)"
        return Var(newValue,newName)

    def sum(self,axis=0):
        newValue = np.sum(self.value,axis=axis)
        newName = f"SUM[{self.name}]"

        return Var(newValue,newName)

    def shape(self):
        newValue = (self.value.shape)
        newName = f"SHAPE[{self.name}]"

        return Var(newValue,newName)
