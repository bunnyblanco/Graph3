import unittest as ut
import graph3
from graph3 import graph
from graph3 import vertex
from graph3 import edge

class testGraph(ut.TestCase):
    """Test the Graph class"""
    def test_graph(self):
        g = graph.Graph()

    def test_nodes(self):
        v = vertex.Vertex('v')
        w = vertex.Vertex('w')
        e = edge.Edge(v, w)
        g = graph.Graph([v, w], [e])

if __name__=='__main__':
    ut.main()
