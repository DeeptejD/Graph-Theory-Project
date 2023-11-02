from plotting_resources import *
from collections import deque
from input import *


class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def dfs(self, node, visited):
        if node not in visited:
            # print(node)
            global prev_node
            if node != prev_node:
                lines.append(
                    returnline(
                        name_to_longlat[prev_node],
                        name_to_longlat[node],
                    )
                )

            visited.add(node)
            for neighbor, _ in self.get_neighbors(node):
                prev_node = node
                global radius
                if (
                    haversine(name_to_longlat[prev_node], name_to_longlat[neighbor])
                    <= radius
                ):
                    self.dfs(neighbor, visited)

    def dfs_traversal(self, start_node):
        visited = set()
        # print("DFS Traversal:")
        self.dfs(start_node, visited)


graph = Graph(adjacency_list)
radius = 30
start_node = "mapusa"
prev_node = "mapusa"
graph.dfs_traversal(start_node)

animate_map()
longlat = name_to_longlat[start_node]
radial_plotting((longlat[1], longlat[0]), radius)


m.save("index.html")
import webbrowser

webbrowser.open("index.html")
