import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue
import numpy as np
from collections import defaultdict
plt.style.use(["science", "notebook", "grid", "dark_background"])
import time


def bfs(graph, start_node, target_node, visited: defaultdict = None):
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
        for neighbour in graph.get(node, []):
            if not visited.get(neighbour, False):
                visited[neighbour] = True
                q.put(neighbour)
    return False, path  # No path found


def create_adjacency_hashmap(edge_list):
    adj_hashmap = defaultdict(list)
    for edge in edge_list:
        adj_hashmap[edge[0]].append(edge[1])
        adj_hashmap[edge[1]].append(edge[0])
    return adj_hashmap


def visualize_search(graph, order, title, pos, adaptive_size:float = 5.0):
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
                node_size=[v * adaptive_size for v in graph.nodes()],
                node_color=colors)
        plt.draw()
        plt.pause(0.5)
    plt.show()
    time.sleep(2)

"""Make a random graph"""
# edge_list = np.random.randint(low = 0, high = 100, size = (200, 2))
# edge_hashmap = create_adjacency_hashmap(edge_list)
# node1 = np.random.randint(low=0, high=100)
# node2 = np.random.randint(low=0, high=100)

# # Create a graph from the adjacency hashmap
# G = nx.Graph()
# for node, neighbors in adj_hashmap.items():
#     for neighbor in neighbors:
#         G.add_edge(node, neighbor)

# print(f"Starting node: {node1}, Target node: {node2}")
# pos = nx.circular_layout(G)
# _, order = bfs(graph=adj_hashmap, start_node=node1, target_node=1e6, visited = defaultdict(bool))
# visualize_search(G, order, adj_hashmap, f"BFS, start = {node1}, target = {node2}", pos)

"""Make a graph with a known path"""
edge_hashmap = {
    1 : [2, 3], 
    2 : [1, 4, 5],
    3 : [1, 6, 7],
    4 : [2, 8, 9],
    5 : [2, 10, 11],
    6 : [3, 12, 13],
    7 : [3, 14, 15]}

# Create a graph from the adjacency hashmap
G = nx.Graph()
for node, neighbors in edge_hashmap.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

pos = nx.spring_layout(G)

_, order = bfs(graph=edge_hashmap, start_node=1, target_node=23, visited = defaultdict(bool))
print(f"Order of traversal = {order}")
visualize_search(G, order, f"BFS, start = {1}, target = {23}", pos, adaptive_size= 10.0)