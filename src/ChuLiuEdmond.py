"""
Chu-liu/Edmond's Algorithm for finding the maximum spanning tree.
"""

from sys import maxsize
from utils.helpers import _reverse_graph, _is_cycle, _get_first, _prune


class ChuLiuEdmond:
    def __init__(self, root, type="minimum") -> None:
        self.root = root
        self.type = type

    def _construct_min_or_max_weighted_graph(self, graph):
        """
        Build the graph.
        Run time: O(|V|*|E|)
        """
        graph_prime = {}
        rev = _reverse_graph(graph)

        for node in rev:
            if node == self.root:
                continue
            if self.type == "minimum":
                index = maxsize
                highest = maxsize
                for edge in rev[node].keys():
                    if rev[node][edge] <= highest:
                        index = edge
                        highest = rev[node][edge]
                graph_prime[node] = {index: highest}
            if self.type == "maximum":
                index = -maxsize
                lowest = -maxsize
                for edge in rev[node].keys():
                    if rev[node][edge] >= lowest:
                        index = edge
                        lowest = rev[node][edge]
                graph_prime[node] = {index: lowest}

        graph_prime[self.root] = {}
        return graph_prime

    def execute(self, Graph):
        """
        Run Chu-liu/Edmond's Algorithm.
        """
        pi = self._construct_min_or_max_weighted_graph(Graph)
        cycle = _is_cycle(pi)
        if not cycle:
            P = _reverse_graph(pi)
            return P

        arbitrary_node_v_c = maxsize
        arbitrary_node_v_c_in_edges = {}
        arbitrary_node_v_c_out_edges = {}

        # D' = <V',E'>
        D_prime = {}

        # The nodes of V' are the nodes of the Graph not in cycle plus a new node denoted arbitrary_node_v_c
        """        
        Not used but according to the algorithm, this is what V' would be:

        V_prime = [set(Graph) - set(cycle)]
        V_prime.append(arbitrary_node_v_c)

        """

        for u in Graph:
            for v in Graph[u]:

                # Three cases specified in the algorithm
                case_1 = (not u in cycle) and (v in cycle)
                case_2 = (u in cycle) and (not v in cycle)
                case_3 = (not u in cycle) and (not v in cycle)

                if case_1:

                    if u not in D_prime:
                        D_prime[u] = {}
                    # According to the algorithm, the weight of Edge(u,v_c) is w(u,v) - w(pi(v),v)
                    w_prime_e = Graph[u][v] - _get_first(pi[v], "value")

                    if (arbitrary_node_v_c not in D_prime[u]) or (
                        arbitrary_node_v_c in D_prime[u] and D_prime[u][arbitrary_node_v_c] > w_prime_e
                    ):
                        # New edge E'(u, arbitrary_node_v_c)
                        D_prime[u][arbitrary_node_v_c] = w_prime_e

                        # Noting in-edges of arbitrary node to take out later
                        arbitrary_node_v_c_in_edges[u] = v

                elif case_2:

                    if arbitrary_node_v_c not in D_prime:
                        # New node arbitrary_node_v_c
                        D_prime[arbitrary_node_v_c] = {}

                    # According to the algorithm, the weight of Edge (v_c,v) e is w(u,v) or Graph[u][v]
                    w_prime_e = Graph[u][v]

                    if (v not in D_prime[arbitrary_node_v_c]) or (
                        v in D_prime[arbitrary_node_v_c] and D_prime[arbitrary_node_v_c][v] > w_prime_e
                    ):
                        # New edge E'(arbitrary_node_v_c, v)
                        D_prime[arbitrary_node_v_c][v] = w_prime_e

                        # Noting out-edges of arbitrary node to take out later
                        arbitrary_node_v_c_out_edges[v] = u

                elif case_3:

                    if u not in D_prime:
                        D_prime[u] = {}

                    D_prime[u][v] = Graph[u][v]

        # Recursively find the min/max arborescence A
        A = self.execute(D_prime)

        A_prime, incoming_node = _prune(
            Graph, A, arbitrary_node_v_c, arbitrary_node_v_c_in_edges, arbitrary_node_v_c_out_edges
        )

        # Remove the edge (π(v),v) from C, breaking the cycle.
        for node in cycle:
            if node != incoming_node:
                first = _get_first(pi[node], "key")
                if not first in A_prime:
                    A_prime[first] = {}
                A_prime[first][node] = pi[node][first]

        return A_prime
