# -------- DELIVERY GRAPH --------
delivery_graph = {
    "Restaurant": ["Street1", "Street2"],
    "Street1": ["Restaurant", "Mall"],
    "Street2": ["Restaurant", "Park"],
    "Mall": ["Street1", "Customer"],
    "Park": ["Street2", "Customer"],
    "Customer": ["Mall", "Park"]
}

# -------- DISPLAY GRAPH --------
def display_graph(graph):
    print("Delivery Area Map:\n")
    for place in graph:
        print(place, "-->", ", ".join(graph[place]))

# -------- DFS FUNCTION --------
def dfs_path(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = []
    if path is None:
        path = []

    visited.append(start)
    path.append(start)

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs_path(graph, neighbor, goal, visited[:], path[:])
            if result:
                return result

    return None

# -------- RUN DFS PROGRAM --------
display_graph(delivery_graph)

print("\nDelivery Route from Restaurant to Customer:")
print(dfs_path(delivery_graph, "Restaurant", "Customer"))
