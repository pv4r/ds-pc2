# ds-pc2

Tarea PC2 - Patrones creacionales (Diseño de Software).

Proyecto del curso: SafeRoute Lima (app de ruteo peatonal seguro).

## Patrones implementados

- **Singleton** (`saferoute/singleton.py`): `GraphLoader` - mantiene el grafo OSM cargado una sola vez en memoria.
- **Factory Method** (`saferoute/factory.py`): `RouteStrategyFactory` - crea estrategias de ruteo (corta, segura, balanceada).

Otros patrones vistos en clase (no implementados): Builder, Prototype, Abstract Factory.

## Correr

```
uv sync
uv run python examples/demo_singleton.py
uv run python examples/demo_factory.py
uv run pytest
```

Referencia: https://github.com/ZapDos7/design-patterns-examples
