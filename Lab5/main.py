import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import algorithm

headers = ['a','b','w']

E = pd.read_csv('aves-barn-swallow-contact-network/aves-barn-swallow-contact-network.edges',header=None ,sep=" ",names=headers )
G = nx.from_pandas_edgelist(E,'a','b',['w'])

pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True)

labels = {e: G[e[0]][e[1]]['w'] for e in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)


print('Number of nodes',algorithm.num_nodes(G),nx.number_of_nodes(G))
print('Number of edges',algorithm.num_edges(G),nx.number_of_edges(G))
print("Density of graph",algorithm.density(G),nx.density(G))
print("Average Degree",algorithm.avg_degree(G))
print("Clustering coeff",algorithm.clustering_coeff(G),nx.clustering(G))
plt.show()
