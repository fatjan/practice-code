def convert_to_adjacency_dict(graph_data):
    graph = {}
    for item in graph_data:
        node, connected_node, _ = item
        if node not in graph:
            graph[node] = []
        if connected_node not in graph:
            graph[connected_node] = []
        graph[node].append(connected_node)
        graph[connected_node].append(node)
    return graph

def can_form_binary_tree(node, parent, graph):
    children_count = 0
    for neighbor in graph[node]:
        if neighbor != parent:
            children_count += 1
            if children_count > 2 or not can_form_binary_tree(neighbor, node, graph):
                return False
    return True

def find_binary_tree_roots(graph_data):
    graph = convert_to_adjacency_dict(graph_data)
    possible_roots = []
    for node in graph:
        if can_form_binary_tree(node, -1, graph):
            possible_roots.append(node)
    return possible_roots

# Given adjacency list
graph_data = [
    [0, 1, 1],  # Node 0 is connected to Node 1 with 1 edge
    [1, 2, 3],  # Node 1 is connected to Node 2 with 3 edges
    [3, 1, 2],  # Node 3 is connected to Node 1 with 2 edges
    [4, 3, 1]   # Node 4 is connected to Node 3 with 1 edge
]

# Find all possible roots for a binary tree
roots = find_binary_tree_roots(graph_data)
print("Possible roots for a binary tree:", roots)
