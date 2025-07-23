import tracyPy as tp
import numpy as np

X_train = np.array([[1, 1, 1],
[0, 0, 1],
 [0, 1, 0],
 [1, 0, 1],
 [1, 1, 1],
 [1, 1, 0],
 [0, 0, 0],
 [1, 1, 0],
 [0, 1, 0],
 [0, 1, 0]])

y_train = np.array([1, 1, 0, 0, 1, 1, 0, 1, 0, 0])
X_train = tp.Var(X_train,"X")
y_train = tp.Var(y_train,"y")

def split(x,y):
    left = y[x==1]
    right = y[x==0]
    return left,right


def purity(y):
    if (y.shape()[0])==0:
        return tp.Var(0,"Y=0")
    return ((y==1).sum())/(y.shape()[0])

def Entropy(x):
    fraction = tp.Var(1e-9,"frac")
    return (-1*x * tp.log2(x+fraction)) - (1-x)*(tp.log2(1-x+fraction))

def wEntropy(root,x):
    return ((x.shape()[0])/(root.shape()[0])) * Entropy(purity(x))

def IG(X,y):
    rootEntropy = []

    for i in range(X.shape().value[1]):
        rootOne = (y_train==1).sum()
        rootS = (X[:,i].shape()[0])
        rootEntropy.append(rootOne/rootS)

    weightedEntropySum = []
    for i in range(X.shape().value[1]):
        root = X[:,i]

        lefty,righty = split(root,y)

        wleft,wright=0,0
        if lefty:
            wleft = wEntropy(root,lefty)
        if righty:
            wright = wEntropy(root,righty)

    rootEntropy = np.asarray(rootEntropy)
    weightedEntropySum = np.asarray(weightedEntropySum)

    return rootEntropy - weightedEntropySum

print(IG(X_train,y_train)[0])
