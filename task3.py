from task1 import G
import networkx as nx


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.nodes()}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)
    
    sorted_distances_dict = dict(sorted(distances.items(), key=lambda item: item[1]))

    return sorted_distances_dict


shortest_path_lengths_from_Colosseum = dijkstra(G, 'Colosseum')
print(f"Shortest path lengths from Colosseum using Dijkstra's algo: {shortest_path_lengths_from_Colosseum}")
