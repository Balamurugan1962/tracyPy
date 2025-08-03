import tracyPy as tp

w = [tp.trace(1,_name=f"w{i}") for i in range(5)]
b = tp.trace(2,_name="b")

x = [tp.trace(1,_name=f"y{i}") for i in range(5)]

y = [(x[i]*w[i] + b )for i in range(5)]

o = 1

tp.draw(y[0])
