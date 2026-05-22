# Patron Factory Method: estrategias de ruteo.
# El usuario elige si quiere la ruta mas corta, la mas segura, o un balance.

from enum import Enum
import networkx as nx


class TipoRuta(str, Enum):
    CORTA = "corta"
    SEGURA = "segura"
    BALANCEADA = "balanceada"


class RutaCorta:
    def calcular(self, g, origen, destino):
        return nx.shortest_path(g, origen, destino, weight="length")


class RutaSegura:
    def calcular(self, g, origen, destino):
        return nx.shortest_path(g, origen, destino, weight="risk_score")


class RutaBalanceada:
    def calcular(self, g, origen, destino):
        def peso(u, v, data):
            return 0.5 * data["length"] + 0.5 * data["risk_score"] * 200
        return nx.shortest_path(g, origen, destino, weight=peso)


class RouteStrategyFactory:
    @staticmethod
    def crear(tipo):
        if tipo == TipoRuta.CORTA:
            return RutaCorta()
        elif tipo == TipoRuta.SEGURA:
            return RutaSegura()
        elif tipo == TipoRuta.BALANCEADA:
            return RutaBalanceada()
        else:
            raise ValueError(f"tipo desconocido: {tipo}")
