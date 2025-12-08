import heapq
import networkx as nx

# --- Створюємо граф із вагами (той самий, що раніше) ---

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
    ("Center", "North_Square", 1.1),
    ("Center", "East_Park", 1.4),
    ("Center", "West_Market", 1.3),
    ("Center", "South_Station", 1.8),
    ("North_Square", "Hill", 0.9),
    ("East_Park", "School", 1.0),
    ("West_Market", "Hospital", 1.6),
    ("South_Station", "River_Bridge", 1.2),
    ("River_Bridge", "West_Market", 0.9),
    ("Industrial", "South_Station", 0.7),
    ("Industrial", "School", 1.9),
    ("Hospital", "North_Square", 1.8),
    ("East_Park", "Hill", 1.2)
]

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# --- алгоритм Дейкстри ---

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph.nodes}
    distances[start] = 0

    prev = {node: None for node in graph.nodes}

    pq = [(0, start)]
    visited = set()

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, prev

# --- Відновлення шляху для Дейкстри ---

def reconstruct_path(prev, start, goal):
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = prev[current]

    path.reverse()

    return path if path[0] == start else None


# Testing 1---------------------------------------------------------------------------------

start = "School"
goal = "Hospital"

distances, prev = dijkstra(G, start)
path = reconstruct_path(prev, start, goal)

print("Найкоротший шлях:", path)
print("Довжина шляху:", distances[goal], "км")
# ------------------------------------------------------------------------------------------

# Testing 2---------------------------------------------------------------------------------

start = "River_Bridge"
goal = "Hill"

distances, prev = dijkstra(G, start)
path = reconstruct_path(prev, start, goal)

print("Найкоротший шлях:", path)
print("Довжина шляху:", distances[goal], "км")
# ------------------------------------------------------------------------------------------

# Testing 3---------------------------------------------------------------------------------

start = "Center"
goal = "Industrial"

distances, prev = dijkstra(G, start)
path = reconstruct_path(prev, start, goal)

print("Найкоротший шлях:", path)
print("Довжина шляху:", distances[goal], "км")
# ------------------------------------------------------------------------------------------

# Testing 4---------------------------------------------------------------------------------

start = "West_Market"
goal = "Industrial"

distances, prev = dijkstra(G, start)
path = reconstruct_path(prev, start, goal)

print("Найкоротший шлях:", path)
print("Довжина шляху:", distances[goal], "км")
# ------------------------------------------------------------------------------------------