# Patron Singleton: GraphLoader.
# El grafo OSM de Lima pesa mucho, no queremos cargarlo en cada request.


class GraphLoader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.graph = None
        return cls._instance

    def cargar(self, grafo):
        if self.graph is None:
            self.graph = grafo
        return self.graph
