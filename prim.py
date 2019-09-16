import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Algortimo de Prim, retorn a MST


def prim(Z, r):
    LAMBDA = []
    PI = []
    Q1 = {}
    Q2 = Z.nodes()
    for v in Q2:
        if v == r:
            LAMBDA.append(0)
            Q1[v] = 0
        else:
            LAMBDA.append(100000000)
            Q1[v] = 100000000
        PI.append(None)
    S = []
    while len(Q1) != 0:
        minimo = min(Q1, key=Q1.get)
        position = Q2.index(minimo)
        q = Q2[position]
        del Q1[minimo]
        S.append(q)
        N = Z.neighbors(q)
        for v in N:
            if v in Q1 and LAMBDA[Q2.index(v)] > Z[q][v]['value']:
                LAMBDA[Q2.index(v)] = Z[q][v]['value']
                Q1[v] = Z[q][v]['value']
                PI[Q2.index(v)] = q

    H = nx.Graph()
    for v in Q2:
        H.add_node(v)
    for i in range(0, len(Q2)):
        if PI[i] != None:
            H.add_edge(PI[i], Q2[i], value=LAMBDA[i])

    return H


# Cria um grafo de teste
G = nx.Graph()
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")
G.add_node("F")
G.add_node("G")
G.add_node("H")
G.add_node("I")

# adiciona as arestas com peso
G.add_edge("A", "B", value=4)
G.add_edge("B", "C", value=8)
G.add_edge("C", "D", value=7)
G.add_edge("D", "E", value=9)
G.add_edge("E", "F", value=10)
G.add_edge("F", "G", value=2)
G.add_edge("H", "I", value=7)
G.add_edge("I", "C", value=2)
G.add_edge("H", "A", value=8)
G.add_edge("B", "H", value=11)
G.add_edge("D", "F", value=14)
G.add_edge("I", "G", value=6)
G.add_edge("F", "C", value=4)
G.add_edge("H", "G", value=1)

# desenha o grafo inicial
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
# Coloca na imagem o peso total
plt.text(0, 1, str(G.size(weight='value')), fontdict=None)
plt.savefig("Graph1.png", format="PNG")
plt.show()
