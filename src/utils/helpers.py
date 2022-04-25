import networkx as nx
import matplotlib.pyplot as plt
from sys import stdin


def read_input():
    graph = {}
    for line in stdin:
        line = line.strip().split()
        u, v, w = line
        try:
            assert int(w)
        except AssertionError:
            print("Error: weight must be a number.")
            return {}
        if not u in graph:
            graph[u] = []
        graph[u].append((v, int(w)))

    for node in graph:
        graph[node] = {i[0]: i[1] for i in graph[node]}
    return graph


def sketch_graph(Graph, MST, type):
    """
    Sketch the graph G.
    Params:
        Graph: the original graph.
        MST: the minimum/maximum spanning tree.
    Return:
        None
    Plots are available on primary desktop.
    """
    G = nx.DiGraph()
    for src in Graph.keys():
        for dst in Graph[src]:
            G.add_edge(src, dst, weight=Graph[src][dst])
    if type == "maximum":
        f = nx.algorithms.tree.maximum_spanning_arborescence(G)
    else:
        f = nx.algorithms.tree.minimum_spanning_arborescence(G)
    plt.figure(3, figsize=(10, 10))
    labels = nx.get_edge_attributes(f, "weight")
    pos = nx.spring_layout(f, seed=50)
    nx.draw_networkx_nodes(f, pos, node_size=700)
    nx.draw_networkx_edges(f, pos, edgelist=f.edges, width=6)
    nx.draw_networkx_labels(f, pos, font_size=20, font_family="sans-serif")
    nx.draw_networkx_edge_labels(f, pos, edge_labels=labels)

    H = nx.DiGraph()
    for src in MST.keys():
        for dst in MST[src]:
            H.add_edge(src, dst, weight=MST[src][dst])

    plt.figure(1, figsize=(10, 10))
    labels = nx.get_edge_attributes(G, "weight")
    pos = nx.spring_layout(G, seed=50)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=6)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.figure(2, figsize=(10, 10))
    labels = nx.get_edge_attributes(H, "weight")
    pos = nx.spring_layout(H, seed=50)
    nx.draw_networkx_nodes(H, pos, node_size=700)
    nx.draw_networkx_edges(H, pos, edgelist=H.edges, width=6)
    nx.draw_networkx_labels(H, pos, font_size=20, font_family="sans-serif")
    nx.draw_networkx_edge_labels(H, pos, edge_labels=labels)

    plt.show()


def _reverse_graph(graph):
    """
    Reverse the graph.
    Params:
        graph: the original graph.
    Return:
        The reversed graph.
    """
    graph_prime = {}
    for node in graph:
        for edge in graph[node].keys():
            if edge not in graph_prime.keys():
                graph_prime[edge] = {}
            graph_prime[edge][node] = graph[node][edge]
    return graph_prime


def _is_cycle(graph):
    """
    Check if the graph has a cycle.
    Params:
        graph: the incoming graph.
    Return:
        First node of cycles if the graph has a cycle, False otherwise.
    Run time: O(|V| + |E|)
    Idea: use DFS to check if there is a cycle.
    Citation for idea of code: https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
    """
    for node in graph:
        # DFS
        visited = list()
        stack = [node]

        while stack:

            item = stack.pop()
            if item in visited:
                cycle = []

                while item not in cycle:
                    cycle.append(item)
                    # get first node of this item's path
                    item = _get_first(graph[item], "key")
                return cycle

            visited.append(item)
            if item in graph:
                all_n_nodes = list(graph[item].keys())
                for item in all_n_nodes:
                    stack.append(item)

    return None


def _get_first(Path, type) -> int:
    """
    Get the first node of the path.
    Params:
        Path: a list of nodes.
        type: "key" or "value".
    Return:
        The weight of the first node of the path.
    """
    # Can't subscript an iterable of .values() or .keys()
    first = []
    if type == "value":
        first = []
        for i in Path.values():
            first.append(i)

    if type == "key":
        for i in Path.keys():
            first.append(i)

    return first[0] if first else None


def _prune(Graph, A, arbitrary_node_v_c, arbitrary_node_v_c_in_edges, arbitrary_node_v_c_out_edges):
    """
    Prune the graph to remove the arbitrary node and its edges that are not in the arborescence.
    Params:
        Graph: the original graph.
        A: the arborescence.
        arbitrary_node_v_c: the arbitrary node.
        arbitrary_node_v_c_in_edges: the in-edges of the arbitrary node.
        arbitrary_node_v_c_out_edges: the out-edges of the arbitrary node.
    Return:
        The pruned graph, in-edge of the arbitrary node
    """
    for node in list(A):
        if node == arbitrary_node_v_c:
            for node_in in A[node]:
                node_out = arbitrary_node_v_c_out_edges[node_in]
                if node_out not in A:
                    A[node_out] = {}
                A[node_out][node_in] = Graph[node_out][node_in]
        else:
            for dst in list(A[node]):
                if dst == arbitrary_node_v_c:
                    new_node_in = arbitrary_node_v_c_in_edges[node]
                    A[node][new_node_in] = Graph[node][new_node_in]
                    del A[node][dst]
    del A[arbitrary_node_v_c]
    return A, new_node_in
