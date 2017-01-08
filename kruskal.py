"""
Kruskal's MST (minimum spanning tree) algorithm

costs can be negative
MST assumes the graph is undirected.
'graph' is defined as: graph = {from:{to:dist, ...}, ...}
if graph[from][to] == dist, it is assumed that graph[to][from] == dist as well
therefore in the MST, the edge would be [from, to, dist] or [to, from, dist]
"""

def init():
    global parent, rank
    parent = {}
    rank = {}

def make_set(node):
    global parent, rank
    parent[node] = node
    rank[node] = 0

def find(node):
    if parent[node] == node:
        return node
    else:
        return find(parent[node])

def union(node1, node2):
    global parent, rank
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        # Attach smaller rank tree under root of higher rank tree
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root2] > rank[root1]:
            parent[root1] = root2
        else:
            # If ranks are same, make one as root and increment its rank by one
            parent[root1] = root2
            rank[root2] += 1
        return True
    else:
        return False

def kruskal(nodes, graph):
    """
    input:   graph   = in dictionary form {from:{to:distance, ...}, ...}
    output:  the MST = list of (head, tail, weight)
    """
    init()
    mst = []
    edges = [[graph[u][v], u, v] for u in graph for v in graph[u]]
    edges = sorted(edges, key=lambda x:x[0])
    for node in nodes:
        make_set(node)
    for length, u, v in edges:
        if union(u, v):
            mst.append((u, v, length))
    return mst


############################
#        E
#       / \
#     1/   \-1
#     D--3--C
#     |     |
#     2     3
#     |     |
#     A--1--B
#

if __name__ == "__main__":
    
    nodes = set(['A', 'B', 'C', 'D', 'E'])
    graph = {'A': {'B':1, 'D':2},
             'B': {'A':1, 'C':3},
             'C': {'B':3, 'D':3, 'E':-1},
             'D': {'A':2, 'C':3, 'E':1},
             'E': {'C':-1, 'D':1}}

    print
    print kruskal(nodes, graph)
    print
