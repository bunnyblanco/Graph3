import unittest as ut
import graph3.vertex as vertex

class testVertex(ut.TestCase):
    """Test the Vertex class"""
    def test_label(self):
        v = vertex.Vertex('v')
        w = vertex.Vertex('w')
        self.assertEqual(v.get_label(), 'v')
        self.assertEqual(w.get_label(), 'w')
        self.assertEqual(v.set_label('r'), 'r')
        self.assertEqual(v.get_label(), 'r')
        self.assertEqual(w.get_label(), 'w')


if __name__=='__main__':
    ut.main()
