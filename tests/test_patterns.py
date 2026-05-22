import networkx as nx
from saferoute.singleton import GraphLoader
from saferoute.factory import (
    RouteStrategyFactory,
    TipoRuta,
    RutaCorta,
    RutaSegura,
    RutaBalanceada,
)


def test_singleton():
    GraphLoader._instance = None
    a = GraphLoader()
    b = GraphLoader()
    assert a is b


def test_factory_corta():
    assert isinstance(RouteStrategyFactory.crear(TipoRuta.CORTA), RutaCorta)


def test_factory_segura():
    assert isinstance(RouteStrategyFactory.crear(TipoRuta.SEGURA), RutaSegura)


def test_factory_balanceada():
    assert isinstance(RouteStrategyFactory.crear(TipoRuta.BALANCEADA), RutaBalanceada)
