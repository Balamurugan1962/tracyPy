import tracyPy as tp
import numpy as np

a = tp.Var(np.array([1,2,3,4],dtype='float64'),"A")
b = tp.Var(np.array([1,2,3,4],dtype='int64'),"B")

c = (a*b)
d = c.dot(a)
e = tp.sin(a)

print(c)
print(d)
print(e)
