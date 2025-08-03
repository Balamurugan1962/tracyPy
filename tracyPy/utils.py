from graphviz import Digraph
import numpy as np




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
        dot.node(name=str(n._id), label = f"{n._name}|value {n.value}" , shape='record')

        if n._op:
            dot.node(name=str(n._id) + n._op, label=n._op)
            dot.edge(str(n._id) + n._op, str(n._id))

    for n1, n2 in edges:
        dot.edge(str(n1._id), str(n2._id) + n2._op)

    dot.render('tree', view=True)
