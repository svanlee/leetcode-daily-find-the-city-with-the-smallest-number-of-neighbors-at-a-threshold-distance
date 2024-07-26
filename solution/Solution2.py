import heapq
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Create an adjacency list to represent the graph
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            # Add edges to the graph in both directions (since it's an undirected graph)
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(city):
            # Initialize distances to all cities as infinity, except for the current city which is 0
            distances = [float('inf')] * n
            distances[city] = 0
            # Create a priority queue with the current city and distance 0
            pq = [(0, city)]
            while pq:
                # Extract the city with the minimum distance from the priority queue
                dist, curr_city = heapq.heappop(pq)
                # Iterate over all neighbors of the current city
                for neighbor, weight in graph[curr_city]:
                    # If a shorter path to the neighbor is found, update the distance and add it to the priority queue
                    if dist + weight < distances[neighbor]:
                        distances[neighbor] = dist + weight
                        heapq.heappush(pq, (dist + weight, neighbor))
            # Return the number of cities that can be reached within the distanceThreshold
            return sum(1 for dist in distances if dist <= distanceThreshold and dist != 0)

        # Find the city with the smallest number of neighbors within the distanceThreshold
        min_neighbors = float('inf')
        res = None
        for city in range(n):
            # Calculate the number of neighbors for the current city
            neighbors = dijkstra(city)
            # If the current city has fewer or equal neighbors, update the result
            if neighbors <= min_neighbors:
                min_neighbors = neighbors
                res = city

        # Return the city with the smallest number of neighbors within the distanceThreshold
        return res