import networkx as nx
import matplotlib.pyplot as plt

class GraphVertex:
    red, blue, black, white = range(4)
    def __init__(self):
        self.color = GraphVertex.white
        self.edges = []

G = [GraphVertex() for _ in range(4)]
G[0].edges.append(G[2])
G[0].edges.append(G[3])
G[1].edges.append(G[2])
G[2].edges.append(G[0])
G[3].edges.append(G[3])

G[0].color = GraphVertex.red
G[1].color = GraphVertex.blue
G[2].color = GraphVertex.black
G[3].color = GraphVertex.white

# Create an empty graph
graph = nx.Graph()

# Add nodes to the graph
for vertex in G:
    graph.add_node(vertex)

# Add edges to the graph
for vertex in G:
    for edge in vertex.edges:
        graph.add_edge(vertex, edge)

# Get the colors of the vertices
node_colors = [vertex.color for vertex in G]
node_colors = ['white', 'red', 'blue', 'black']

# Draw the graph
nx.draw(graph, with_labels=True, node_color=node_colors, edge_color='gray', font_weight='bold')

# Display the graph
plt.show()