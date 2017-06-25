import unittest as ut
from graph3 import edge, vertex, graph

class Graph_Tests(ut.TestCase):
    def setUp(self):
        self.v = vertex.Vertex('v')
        self.w = vertex.Vertex('w')
        self.e = edge.Edge(self.v, self.w)
        self.g = graph.Graph([self.v,self.w], [self.e])

    def test_nodes(self):
        vs = list(self.g.keys())
        self.assertEqual(len(vs),2)
        self.assertIn(self.v, vs)
        self.assertIn(self.w,vs)

    def test_edges(self):
        es = self.g.get_edge(self.e)
        for e in es:
            self.assertIn(str(e),["Edge(Vertex('v'), Vertex('w'))","Edge(Vertex('w'), Vertex('v'))"])

