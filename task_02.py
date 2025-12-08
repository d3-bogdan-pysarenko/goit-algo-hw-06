import networkx as nx
from collections import deque

# --- Створення графа (той самий, що й раніше) ---

G = nx.Graph()

nodes = {
    "Center": (0, 0),
    "North_Square": (0, 2),
    "East_Park": (2, 0.5),
    "West_Market": (-2, 0.5),
    "South_Station": (0, -2),
    "Hill": (1.5, 2.2),
    "River_Bridge": (-1.5, -1.2),
    "School": (2.8, -0.4),
    "Hospital": (-2.6, 1.4),
    "Industrial": (0.8, -2.5)
}

for n, pos in nodes.items():
    G.add_node(n)

edges = [
    ("Center", "North_Square"),
    ("Center", "East_Park"),
    ("Center", "West_Market"),
    ("Center", "South_Station"),
    ("North_Square", "Hill"),
    ("East_Park", "School"),
    ("West_Market", "Hospital"),
    ("South_Station", "River_Bridge"),
    ("River_Bridge", "West_Market"),
    ("Industrial", "South_Station"),
    ("Industrial", "School"),
    ("Hospital", "North_Square"),
    ("East_Park", "Hill")
]

G.add_edges_from(edges)


# --------------------------------------------- DFS -----------------------------------------------------------

def dfs_path(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == goal:
        return path.copy()

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs_path(graph, neighbor, goal, visited, path)
            if result is not None:
                return result

    path.pop()
    return None


# --------------------------------------------- BFS -----------------------------------------------------------

def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


# --------------------------------------------- Testing -----------------------------------------------------------

start = "Hospital"
goal = "School"

dfs_result = dfs_path(G, start, goal)
bfs_result = bfs_path(G, start, goal)

print("DFS шлях:", dfs_result)
print("BFS шлях:", bfs_result)
