from task1 import G
from collections import deque


def dfs_recursive(graph, vertex, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(vertex)
    result.append(vertex)  

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)
    
    return result 

def bfs_recursive(graph, queue, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    if not queue:
        return result
    
    vertex = queue.popleft()

    if vertex not in visited:
        visited.add(vertex)
        result.append(vertex)
        queue.extend(set(graph[vertex]) - visited)

    return bfs_recursive(graph, queue, visited, result)


dfs_result = dfs_recursive(G, 'Colosseum')
print(f"DFS algo result: {dfs_result}")

bfs_result = bfs_recursive(G, deque(["Colosseum"]))
print(f"BFS algo result: {bfs_result}")
