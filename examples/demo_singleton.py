import networkx as nx
from saferoute.singleton import GraphLoader


def grafo_demo():
    g = nx.DiGraph()
    g.add_edge(0, 1, length=50, risk_score=1.0)
    g.add_edge(1, 4, length=50, risk_score=1.0)
    g.add_edge(0, 2, length=250, risk_score=0.25)
    g.add_edge(2, 4, length=250, risk_score=0.25)
    g.add_edge(0, 3, length=100, risk_score=0.5)
    g.add_edge(3, 4, length=100, risk_score=0.5)
    return g


a = GraphLoader()
b = GraphLoader()

print("a is b:", a is b)

a.cargar(grafo_demo())
b.cargar(grafo_demo())  # no recarga

print("a.graph is b.graph:", a.graph is b.graph)
print("nodos:", list(a.graph.nodes))
