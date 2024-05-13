import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_nodes_from(["Great Wall of China", "Christ the Redeemer", "Petra", "Machu Picchu", "Chichen Itza", "Taj Mahal", "Colosseum"])
G.add_weighted_edges_from([
    ('Great Wall of China', 'Chichen Itza', 12757),  
    ('Great Wall of China', 'Taj Mahal', 3821),
    ('Petra', 'Taj Mahal', 4151),
    ('Petra', 'Colosseum', 2421),
    ('Christ the Redeemer', 'Colosseum', 9184),
    ('Christ the Redeemer', 'Chichen Itza', 6895), 
    ('Machu Picchu', 'Chichen Itza', 4134),  
    ('Christ the Redeemer', 'Machu Picchu', 3281), 
    ('Taj Mahal', 'Colosseum', 6084)])


num_nodes = G.number_of_nodes() 
num_edges = G.number_of_edges()  
is_connected = nx.is_connected(G)  

degree_centrality = nx.degree_centrality(G)  
closeness_centrality = nx.closeness_centrality(G)  
betweenness_centrality = nx.betweenness_centrality(G) 


if __name__ == '__main__':

    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")
    print(f"Is the graph connected? {is_connected}")

    print(f"Degree Centrality: {degree_centrality}")
    print(f"Closeness Centrality: {closeness_centrality}")
    print(f"Betweenness Centrality: {betweenness_centrality}")

    pos = nx.shell_layout(G)
    plt.figure(figsize=(9, 9))
    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=2000)
    nx.draw_networkx_edges(G, pos, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d['weight']} km" for u, v, d in G.edges(data=True)}, font_size=6, font_color='red')
    nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')
    plt.title('Trip Between the New Seven Wonders of the World')
    plt.axis('off')  
    plt.show()
