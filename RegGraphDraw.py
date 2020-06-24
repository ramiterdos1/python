import networkx as nx

def create4degGraph(inp) :
    G=nx.Graph()
    G.add_nodes_from([i for i in range(inp)])
    for i in range(inp) :
       G.add_edge(i,(i+1) % (inp))
       G.add_edge(i,(i+2) % (inp))
    return G

def cliqueGraph(inp) :
    G=nx.Graph()
    G.add_nodes_from([i for i in range(inp)])
    for i in range(inp) :
       for j in range(inp/2) :
          G.add_edge(i,(i+j+1) % (inp))
    return G

def degGraph(inp,deg) :
    G=nx.Graph()
    G.add_nodes_from([i for i in range(inp)])
    for i in range(inp) :
       for j in range(deg) :
          G.add_edge(i,(i+j+1) % (inp))
    return G


