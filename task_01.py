import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф
G = nx.Graph()

# Cootdinates
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

# Nodes
for n, pos in nodes.items():
    G.add_node(
        n,
        pos=pos,
        kind=("bus_stop" if n in ["South_Station", "North_Square"] else "intersection")
    )

# roads
edges = [
    ("Center", "North_Square", 1.1, ["road","bus"]),
    ("Center", "East_Park", 1.4, ["road","bus"]),
    ("Center", "West_Market", 1.3, ["road"]),
    ("Center", "South_Station", 1.8, ["road","bus"]),
    ("North_Square", "Hill", 0.9, ["road"]),
    ("East_Park", "School", 1.0, ["road","bus"]),
    ("West_Market", "Hospital", 1.6, ["road"]),
    ("South_Station", "River_Bridge", 1.2, ["road"]),
    ("River_Bridge", "West_Market", 0.9, ["road"]),
    ("Industrial", "South_Station", 0.7, ["road"]),
    ("Industrial", "School", 1.9, ["road"]),
    ("Hospital", "North_Square", 1.8, ["road","bus"]),
    ("East_Park", "Hill", 1.2, ["road"])
]

for u, v, dist, modes in edges:
    G.add_edge(u, v, distance_km=dist, modes=modes)

# Nodes position
pos = nx.get_node_attributes(G, 'pos')

# draw
plt.figure(figsize=(10, 8))
plt.title("Transport infrastructure model of the Silent Hill city", fontsize=16)

# listing
road_edges = [(u, v) for u, v, d in G.edges(data=True) if "road" in d['modes']]
bus_edges  = [(u, v) for u, v, d in G.edges(data=True) if "bus" in d['modes']]

# Nodes types
intersections = [n for n, d in G.nodes(data=True) if d["kind"] == "intersection"]
bus_stops     = [n for n, d in G.nodes(data=True) if d["kind"] == "bus_stop"]

# Different type of edges draw
nx.draw_networkx_nodes(G, pos, nodelist=intersections, node_size=450)
nx.draw_networkx_nodes(G, pos, nodelist=bus_stops, node_shape='s', node_size=600)

# Малюємо дороги і автобусні маршрути
nx.draw_networkx_edges(G, pos, edgelist=road_edges, width=2)
nx.draw_networkx_edges(G, pos, edgelist=bus_edges, width=5, style='dashed')

# Edges signature
nx.draw_networkx_labels(G, pos, font_size=9)

# Distance signing
edge_labels = {(u, v): f"{d['distance_km']} km" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# show
plt.show()

# Analisys
"""
Створений граф містить:
- 10 транспортних вузлів (вершин)
- 13 доріг та маршрутів(ребер)
- окремі позначення для автобусних зупинок(квадратами)
- жирні пунктирні лінії для автобусних маршрутів
- відстані підписані відстані в км
"""