import unittest as ut
import graph3
from graph3 import edge
from graph3 import vertex

class testEdge(ut.TestCase):
    """Test the Edge class"""
    def test_nodes(self):
        v = vertex.Vertex('v')
        w = vertex.Vertex('w')
        e = edge.Edge(v, w)
        self.assertEqual(e[0].get_label(),'v')
        self.assertEqual(e[1].get_label(),'w')

if __name__=='__main__':
    ut.main()
