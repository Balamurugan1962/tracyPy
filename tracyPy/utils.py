from graphviz import Digraph
from .trace import trace
import numpy as np


def sum(self):
    return trace(self.value.sum(),[self],"SUM",f"SU([{self._name})")

def dot(self,other):
    return trace(np.dot(self.value,other.value),(self,other),"DOT",f"DOT({self._name})")

def sin(self):
    return trace(np.sin(self.value),[self],"SIN",f"SIN({self._name})")


def matmul(self,other):
    return trace(np.matmul(self.value,other.value),(self,other),"MATMUL",f"MATMUL({self._name})")


def draw(root, format='pdf', rankdir='LR'):
    def trace(root):
        nodes,edges = [],[]
        visited = []

        st = []
        st.append(root)
        nodes.append(root)


        while(len(st)!=0):
            v = st[-1]
            st.pop()

            for child in v._prev:
                nodes.append(child)
                edges.append((child,v))
                visited.append(child)
                st.append(child)

        return nodes,edges

    assert rankdir in ['LR', 'TB']

    nodes, edges = trace(root)

    dot = Digraph(format=format, graph_attr={'rankdir': rankdir})

    for n in nodes:
        dot.node(name=str(n._id), label = f"{n._name}" , shape='record')

        if n._op:
            dot.node(name=str(n._id) + n._op, label=n._op)
            dot.edge(str(n._id) + n._op, str(n._id))

    for n1, n2 in edges:
        dot.edge(str(n1._id), str(n2._id) + n2._op)

    dot.render('tree', view=True)
