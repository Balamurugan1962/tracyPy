import tracyPy as tp
from tracyPy import trace as t
import numpy as np
import matplotlib.pyplot as plt

class Linear:
    def __call__(self,A):
        return A

class Dense:
    def __init__(self,units,in_features,activation):
        self.units = units
        self.in_features = in_features

        self.W = t(np.random.randn(in_features,units));self.W._name = "W"
        self.B = t(np.random.randn(1,units));self.B._name = "B"

        self.g = activation

    def __call__(self,X):
        if X.shape[1] != self.W.shape[0]:
            raise ValueError(f"Invalid Input dim {X.shape}, {self.W.shape}")

        Z = tp.matmul(X,self.W) + self.B
        A = self.g(Z)

        return A


x = np.linspace(-2 * np.pi, 2 * np.pi, 800)
y = np.sin(x) + 0.1 * np.random.randn(len(x))

xt = np.linspace(-2 * np.pi, 2 * np.pi, 200)
yt = np.sin(xt) + 0.1 * np.random.randn(len(xt))


X_train = x.reshape(-1,1)
y_train = y.reshape(-1,1)

X_test = xt.reshape(-1,1)
y_test = yt.reshape(-1,1)
# normalisation
max_val = np.max(X_train)
max_val = max(max_val,np.max(X_test))

X_train = X_train / max_val
X_test = X_test / max_val

X_train = t(X_train);X_train._name = "X"
y_train = t(y_train);y_train._name = "y"

X_test = t(X_test);X_test._name = "Xt"
y_test = t(y_test);y_test._name = "yt"

x = t(np.array([[1]]));x._name="x"
layer1 = Dense(2,1,Linear())
layer2 = Dense(1,2,Linear())

y1 = layer1(x)
y2 = layer2(y1)

tp.draw(y2)
