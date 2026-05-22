import networkx as nx
from saferoute.factory import RouteStrategyFactory, TipoRuta


g = nx.DiGraph()
g.add_edge(0, 1, length=50, risk_score=1.0)
g.add_edge(1, 4, length=50, risk_score=1.0)
g.add_edge(0, 2, length=250, risk_score=0.25)
g.add_edge(2, 4, length=250, risk_score=0.25)
g.add_edge(0, 3, length=100, risk_score=0.5)
g.add_edge(3, 4, length=100, risk_score=0.5)


for tipo in TipoRuta:
    estrategia = RouteStrategyFactory.crear(tipo)
    ruta = estrategia.calcular(g, 0, 4)
    print(f"{tipo.value}: {ruta}")
