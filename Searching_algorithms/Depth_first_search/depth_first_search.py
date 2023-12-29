import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time
plt.style.use(["science", "notebook", "grid"])


edge_list = []
for _ in range(150):
    node1, node2 = np.random.randint(low = 0, high = 50, size = 2)
    edge_list.append((node1, node2))


G = nx.Graph()
G.add_edges_from(edge_list)


def dfs(graph, start_node, target_node, visited=None):
    if visited is None:
        visited = []
    visited.append(start_node)
    if start_node == target_node:
        return visited
    for neighbor in graph.neighbors(start_node):
        if neighbor not in visited:
            path = dfs(graph, neighbor, target_node, visited)
            if path is not None:
                return path
    return None


def visualize_search(graph, order, title, pos):
    plt.figure(figsize = (15, 8))
    plt.title(title, fontsize = 15, fontweight = "bold")
    visited = []
    for idx, node in enumerate(order):
        plt.clf()
        title = f"DFS, start = {node1}, target = {node2}, current node = {node}"
        plt.title(title, fontsize = 15, fontweight = "bold")
        visited.append(node)
        colors = []
        for n in graph.nodes:
            if n in visited:
                colors.append("r")
            else:
                colors.append("g")
        nx.draw(G, pos, with_labels = True, 
                node_size=[v * 5 for v in graph.nodes()], 
                node_color = colors)
        plt.draw()
        plt.pause(0.5)
    plt.show()
    time.sleep(1)



pos = nx.spring_layout(G, scale=10)
print(f"Starting node: {node1}, Target node: {node2}")
order = dfs(graph=G, start_node=node1, target_node=node2)
visualize_search(G, order, f"DFS, start = {node1}, target = {node2}", pos)