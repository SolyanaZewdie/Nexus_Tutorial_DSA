import heapq

class Solution(object):
    def processQueries(self, c, connections, queries):
        parent = list(range(c + 1))
        rank = [0] * (c + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1

        for u, v in connections:
            union(u, v)

        groups = {}
        for i in range(1, c + 1):
            root = find(i)
            if root not in groups:
                groups[root] = []
            heapq.heappush(groups[root], i)

        offline = set()
        res = []

        for t, x in queries:
            if t == 1:
                if x not in offline:
                    res.append(x)
                else:
                    root = find(x)
                    while groups[root] and groups[root][0] in offline:
                        heapq.heappop(groups[root])
                    res.append(groups[root][0] if groups[root] else -1)
            else:
                offline.add(x)

        return res
