import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()

    def buildGraph(self):
        allLocalizations = DAO.getAllLocalizations()
        self._grafo.add_nodes_from(allLocalizations)
        self.addEdges()
        return True

    def addEdges(self):
        allConnessioni = DAO.getAllConnections()
        for c in allConnessioni:
            self._grafo.add_edge(c.l1, c.l2, weight=c.peso)

    def compConn(self, origine):
        connComp = self._grafo.neighbors(origine)
        mappa = {}
        for c in connComp:
            mappa[c] = self._grafo[origine][c]['weight']
        return mappa


    def printGraphDetails(self):
        return f"{len(self._grafo.nodes)} vertici, {len(self._grafo.edges)} archi"

    def getNodes(self):
        return self._grafo.nodes
