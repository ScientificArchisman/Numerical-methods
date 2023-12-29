import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from queue import Queue
from collections import defaultdict
plt.style.use(["science", "notebook", "grid", "dark_background"])
import time


def bfs(graph, start_node, target_node, visited = None):
    q = Queue()
    path = []
    visited[start_node] = True
    q.put(start_node)
    path.append(start_node)
    while not q.empty():
        node = q.get()
        path.append(node)
        if node == target_node:
            return True, path
        for neighbour in graph[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                q.put(neighbour)
    return False, path  # No path found


def create_adjacency_hashmap(edge_list):
    adj_hashmap = defaultdict(list)
    for edge in edge_list:
        adj_hashmap[edge[0]].append(edge[1])
        adj_hashmap[edge[1]].append(edge[0])
    return adj_hashmap


def visualize_search(graph, order, adjacency_hashmap, title, pos):
    plt.figure(figsize = (15, 8))
    plt.title(title, fontsize = 15, fontweight = "bold")
    visited = []

    if len(order) == 1:
        nx.draw(graph, pos, with_labels=True,
                node_size=[v * 5 for v in graph.nodes()],
                node_color="r")
        plt.draw()
        plt.pause(0.5)
        return

    for node in order:
        plt.clf()
        title = f"current node = {node}"
        plt.title(title, fontsize = 15, fontweight = "bold")
        visited.append(node)
        colors = []
        for n in graph.nodes:
            if n in visited:
                colors.append("r")
            else:
                colors.append("g")
        nx.draw(graph, pos, with_labels=True,
                node_size=[v * 5 for v in graph.nodes()],
                node_color=colors)
        plt.draw()
        plt.pause(0.5)
    plt.show()
    time.sleep(1)

edge_list = np.random.randint(low = 0, high = 100, size = (200, 2))
adj_hashmap = create_adjacency_hashmap(edge_list)
node1 = np.random.randint(low=0, high=100)
node2 = np.random.randint(low=0, high=100)

# Create a graph from the adjacency hashmap
G = nx.Graph()
for node, neighbors in adj_hashmap.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

print(f"Starting node: {node1}, Target node: {node2}")
pos = nx.circular_layout(G)
_, order = bfs(graph=adj_hashmap, start_node=node1, target_node=1e6, visited = defaultdict(bool))
visualize_search(G, order, adj_hashmap, f"BFS, start = {node1}, target = {node2}", pos)
