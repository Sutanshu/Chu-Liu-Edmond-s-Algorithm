from ChuLiuEdmond import ChuLiuEdmond
from utils.helpers import sketch_graph, read_input
from adHocSanityTest import getTotal
import sys


def main(input_graph={}, type="minimum", root="a", sketch=True):

    Graph = {
        "a": {"b": 7, "c": 9, "d": 12},
        "b": {"e": 53, "f": 2},
        "c": {"d": 1, "f": 99},
        "d": {"b": 76},
        "e": {"c": 39},
    }
    chu_liu_edmond = ChuLiuEdmond(root, type)
    graph_prime = chu_liu_edmond.execute(input_graph if input_graph else Graph)
    if sketch:
        sketch_graph(input_graph if input_graph else Graph, graph_prime, type)
    if not sketch:
        print("MST: ", graph_prime)


if __name__ == "__main__":
    flags = ["maximum", "custom_input_graph", 'root="a"']
    if "sketch" in sys.argv:
        if "custom_input_graph" in sys.argv:
            root = sys.argv[-1].split("=")[-1]
            if "maximum" in sys.argv:
                main(read_input(), type="maximum", root=root, sketch=True)
            else:
                main(read_input(), type="minimum", root=root, sketch=True)

        elif "maximum" in sys.argv and (not "custom_input_graph" in sys.argv):
            main(type="maximum", sketch=True)

        else:
            main()
    else:
        if "custom_input_graph" in sys.argv:
            root = sys.argv[-1].split("=")[-1]
            if "maximum" in sys.argv:
                main(read_input(), type="maximum", root=root, sketch=False)
            else:
                main(read_input(), type="minimum", root=root, sketch=False)

        elif "maximum" in sys.argv and (not "custom_input_graph" in sys.argv):
            main(type="maximum", sketch=False)

        else:
            main(sketch=False)
