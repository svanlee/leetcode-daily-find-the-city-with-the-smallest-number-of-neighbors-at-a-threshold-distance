import heapq
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Create an adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(city):
            distances = [float('inf')] * n
            distances[city] = 0
            pq = [(0, city)]
            while pq:
                dist, curr_city = heapq.heappop(pq)
                for neighbor, weight in graph[curr_city]:
                    if dist + weight < distances[neighbor]:
                        distances[neighbor] = dist + weight
                        heapq.heappush(pq, (dist + weight, neighbor))
            return sum(1 for dist in distances if dist <= distanceThreshold and dist != 0)

        # Find the city with the smallest number of neighbors within the distanceThreshold
        min_neighbors = float('inf')
        result = -1
        for city in range(n):
            neighbors = dijkstra(city)
            if neighbors <= min_neighbors:
                min_neighbors = neighbors
                result = city

        return result