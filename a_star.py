import heapq

def a_star(graph,heuristics,start,goal):
    open_list = []
    heapq.heappush(open_list,(0,start))

    g_cost = {node:float('inf') for node in graph}
    g_cost[start] = 0

    parent = {start: None}

    while open_list:
        current_f,current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1],g_cost[goal]

        for neighbor ,cost in graph[current]:
            tentative_g = g_cost[current] + cost

            if tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristics[neighbor]
                heapq.heappush(open_list,(f_cost,neighbor))
                parent[neighbor] = current

    return None,float('inf')


graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('B', 3),('D', 1),('E', 5)],
    'D': [('C', 1),('E', 8),('B',2)],
    'E': [('C', 5),('J', 5),('I',5),('D',8)],
    'F': [('G', 1),('H',7)],
    'G': [('I',3)],
    'H': [('I', 2),('F',7)],
    'I': [('G', 3),('H',2),('E',5),('J',3)],
    'J': [('E',5),('I',3)]
}
heuristics = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0,
}
start_node = 'A'
goal_node = 'J'

path, cost = a_star(graph, heuristics, start_node, goal_node)

print("Shortest Path:", path)
print("Total Cost:", cost)
