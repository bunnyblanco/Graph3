import unittest as ut
from graph3 import edge
from graph3 import vertex

class Component_Tests(ut.TestCase):
    """Test the components of a Graph"""
    def setUp(self):
        self.v = vertex.Vertex(label='v')
        self.w = vertex.Vertex(label='w')
        self.e = edge.Edge(self.v, self.w)

    def test_nodes(self):
        self.assertEqual(self.v.label,'v')
        self.assertEqual(str(self.v),"Vertex('v')")
        self.assertEqual(self.w.label,'w')
        self.assertEqual(str(self.w),"Vertex('w')")

    def test_edge(self):
        self.assertIn(self.v,self.e)
        self.assertIn(self.w,self.e)
        self.assertEqual(str(self.e), "Edge(Vertex('v'), Vertex('w'))")

if(__name__=='__main__'):
    ut.main()
