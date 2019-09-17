import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


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


# Cria um grafo de teste que resultara na imagem PNG

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

# Adiciona as arestas com peso que desejar

G.add_edge("A", "B", value=6)
G.add_edge("B", "C", value=4)
G.add_edge("C", "D", value=5)
G.add_edge("D", "E", value=10)
G.add_edge("E", "F", value=11)
G.add_edge("F", "G", value=4)
G.add_edge("H", "I", value=3)
G.add_edge("A", "F", value=1)
G.add_edge("B", "H", value=8)
G.add_edge("D", "A", value=12)
G.add_edge("I", "C", value=15)
G.add_edge("G", "C", value=16)
G.add_edge("C", "F", value=14)
G.add_edge("H", "G", value=7)

# Desenha o grafo inicial

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)

# Coloca na imagem

plt.text(0, 1, str(G.size(weight='value')), fontdict=None)
plt.savefig("Graph1.png", format="PNG")
plt.show()
