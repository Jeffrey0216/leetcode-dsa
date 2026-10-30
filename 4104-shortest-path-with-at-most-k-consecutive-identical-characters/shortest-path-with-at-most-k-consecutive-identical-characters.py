import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:

        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        # dist[node][consecutive_count]
        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        pq = [(0, 0, 1)]

        dist[0][1] = 0

        while pq:
            cost, node, count = heapq.heappop(pq)

            if cost > dist[node][count]:
                continue

            if node == n - 1:
                return cost

            for nei, wt in adj[node]:

                if labels[node] == labels[nei]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + wt

                if new_cost < dist[nei][new_count]:
                    dist[nei][new_count] = new_cost

                    heapq.heappush(
                        pq,
                        (new_cost, nei, new_count)
                    )

        return -1  