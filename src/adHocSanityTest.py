from ChuLiuEdmond import ChuLiuEdmond
import networkx as nx
from random import randint
import time


def main():
    Graph = {
        "a": {"b": randint(0, 100), "c": randint(0, 100), "d": randint(0, 100)},
        "b": {"e": randint(0, 100), "f": randint(0, 100)},
        "c": {"d": randint(0, 100), "f": randint(0, 100)},
        "d": {"b": randint(0, 100)},
        "e": {"c": randint(0, 100)},
    }

    check_min_spanning_tree(Graph)
    check_max_spanning_tree(Graph)


def check_min_spanning_tree(Graph):

    root = "a"
    type = "minimum"
    chu_liu_edmond = ChuLiuEdmond(root, type)
    t_1 = time.time()
    myMST = chu_liu_edmond.execute(Graph)
    t_2 = time.time()
    print("Time taken by my implementation: ", t_2 - t_1)

    G = nx.DiGraph()
    for src in Graph.keys():
        for dst in Graph[src]:
            G.add_edge(src, dst, weight=Graph[src][dst])

    H = nx.DiGraph()
    for src in myMST:
        for dst in myMST[src]:
            H.add_edge(src, dst, weight=myMST[src][dst])

    t_1 = time.time()
    libMST = nx.algorithms.tree.minimum_spanning_arborescence(G)
    t_2 = time.time()
    print("Time taken by standard library: ", t_2 - t_1)

    try:
        assert getTotal(H.edges, Graph) == getTotal(libMST.edges, Graph)
        print("Total is: ", getTotal(H.edges, Graph))
        print("Minimum spanning tree is correct!")

    except AssertionError:
        print("Error: MSTs are not equal!")


def check_max_spanning_tree(Graph):
    root = "a"
    type = "maximum"
    chu_liu_edmond = ChuLiuEdmond(root, type)
    t_1 = time.time()
    myMST = chu_liu_edmond.execute(Graph)
    t_2 = time.time()
    print("Time taken by my implementation: ", t_2 - t_1)

    G = nx.DiGraph()
    for src in Graph.keys():
        for dst in Graph[src]:
            G.add_edge(src, dst, weight=Graph[src][dst])

    H = nx.DiGraph()
    for src in myMST:
        for dst in myMST[src]:
            H.add_edge(src, dst, weight=myMST[src][dst])

    t_1 = time.time()
    libMST = nx.algorithms.tree.maximum_spanning_arborescence(G)
    t_2 = time.time()
    print("Time taken by standard library: ", t_2 - t_1)
    try:
        assert getTotal(H.edges, Graph) == getTotal(libMST.edges, Graph)
        print("Total is: ", getTotal(H.edges, Graph), getTotal(libMST.edges, Graph))
        print("Maximum spanning tree is correct!")

    except AssertionError:
        print("Error: MSTs are not equal!")


def getTotal(affected_graph, original_graph):
    total = 0
    for i in affected_graph:
        total += original_graph[i[0]][i[1]]
    return total


if __name__ == "__main__":
    main()
