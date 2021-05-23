from UnionFind import WeightedPathCompressedQuickUnion as QuickUnion


class Kruskals:

    # Assume edges are tuples of form (a, b, w)
    # Where a and b are vertices and w is the weight of the edge between them.

    def __init__(self, edges, vertices):
        self.edges = edges
        self.vertices = vertices

        self.sort()
        self.solve()
        print("Solved")

    def sort(self):
        # Sort the edges into ascending weights
        self.edges = sorted(self.edges, key=lambda x: x[2])

    def solve(self):
        tree = QuickUnion(len(self.vertices))
        for edge in self.edges:
            # Check nodes are not already connected (avoid cycles)
            if not tree.is_connected(edge[0], edge[1]):
                tree.union(edge[0], edge[1])
                print("Joined edge " + str(edge))

            solved = True
            n = tree.root(self.vertices[0])
            for i in range(1, len(self.vertices)):
                if n != tree.root(self.vertices[i]):
                    solved = False
                    break

            if solved:
                return
