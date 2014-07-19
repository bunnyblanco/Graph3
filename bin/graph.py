""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""
import graph3.vertex as vertex
import graph3.edge as edge
import graph3.graph as graph

if __name__=="__main__":
    v = vertex.Vertex('v')
    print(v)
    w = vertex.Vertex('w')
    print(w)
    e = edge.Edge(v, w)
    print(e)
    g = graph.Graph([v,w], [e])
    print(g)


