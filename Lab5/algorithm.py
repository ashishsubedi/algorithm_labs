import numpy as np
import networkx as nx

def num_nodes(G):
    return len(nx.nodes(G))

def num_edges(G):
    return len(nx.edges(G))

def density(G):
    e = num_edges(G)
    v = num_nodes(G)
    d = (2*e)/(v*(v-1))
    return d

def degree(G,v):
    return len(G.adj[v])

def avg_degree(G):
    count = 0
    for v in G.nodes:
       count += degree(G,v)

    v = num_nodes(G)
    return (count/v)


def diameter(G):
    pass

def clustering_coeff(G):
    C = {}
    for i in G.nodes:
        k = len(G.adj[i])
        if(k<2): 
            C[i] = 0
            continue

        e = 0
        
        for v in G.adj[i]:

            for u in G.adj[i]:
                if(v==u): continue

                if(G.has_edge(u,v)):
                    e+=1
        e = e/2
        C[i] = (2*e)/(k*(k-1)) 
    return C
def clustering_coeff_V2(G):
    C = {}
    for i in G.nodes:
        k = len(G.adj[i])
        if(k<2): 
            C[i] = 0
            continue

        e = 0
        
        H = G.subgraph([i]+G.adj[i])
        e = len(num_edges(G))
        C[i] = (2*e)/(k*(k-1)) 
    return C
