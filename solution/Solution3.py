import heapq
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Create an adjacency list to represent the graph
        adj = {i: dict() for i in range(n)}
        for u, v, d in edges:
            # Only consider edges with distance less than or equal to the distanceThreshold
            if d <= distanceThreshold:
                adj[u][v] = d
                adj[v][u] = d
        
        # Initialize a list to store the number of cities that can be reached from each city
        cities = [0] * n
        for i in range(n):
            # Initialize variables for the current city
            count = -1  # count of cities that can be reached
            distance = [float('inf')] * n  # distances to all cities
            distance[i] = 0  # distance to the current city is 0
            visited = [False] * n  # visited cities

            # Create a priority queue with the current city and distance 0
            pq = [(0, i)]
            heapq.heapify(pq)

            while pq:
                # Extract the city with the minimum distance from the priority queue
                d, node = heapq.heappop(pq)
                if d > distanceThreshold:
                    # If the distance exceeds the threshold, break the loop
                    break
                if visited[node]:
                    # If the city has already been visited, skip it
                    continue
                visited[node] = True
                count += 1  # increment the count of reachable cities
                for v in adj[node]:
                    # Iterate over all neighbors of the current city
                    if not visited[v] and d + adj[node][v] < distance[v]:
                        # If a shorter path to the neighbor is found, update the distance and add it to the priority queue
                        distance[v] = d + adj[node][v]
                        heapq.heappush(pq, (distance[v], v))
            cities[i] = count  # store the count of reachable cities for the current city

        # Find the city with the smallest number of reachable cities
        max_node = 0
        min_distance = cities[0]
        for i in range(n):
            if cities[i] <= min_distance:
                max_node = i
                min_distance = cities[i]
        return max_node  # return the city with the smallest number of reachable cities