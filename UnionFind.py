class WeightedPathCompressedQuickUnion:

    def __init__(self, n):
        # Initialise id array and size array (for weighted quick union)
        self.id = [i for i in range(n)]
        self.size = [1] * n

    def root(self, i):
        # Store the path taken to find the root to do path compression later
        path = []
        while i != self.id[i]:
            path.append(i)
            i = self.id[i]

        # Compress the path, to increase speed of future searches
        for p in path:
            self.id[p] = i

        return i

    def is_connected(self, p, q):
        return self.root(p) == self.root(q)

    def find(self, p):
        return self.root(p)

    # Weighted Quick Union
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        # Add the smaller tree to the root of the larger tree to keep the tree balanced.
        if self.size[i] < self.size[j]:
            self.id[i] = self.id[j]
            self.size[j] += self.size[i]
        else:
            self.id[j] = self.id[i]
            self.size[i] += self.size[j]
