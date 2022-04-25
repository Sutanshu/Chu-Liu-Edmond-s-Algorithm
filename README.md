# Chu-Liu-Edmond-s-Algorithm

This algorithm is an implementation of the [**Chu-Liu-Edmond**](https://en.wikipedia.org/wiki/Chu%E2%80%93Liu-Edmonds_algorithm) algorithm. It finds the minimum and maximum spanning tree of a directed graph. The running time is O(|V|*|E|). The running time of individual functions is mentioned in the code. 

Steps:
git clone https://github.com/Sutanshu/Chu-Liu-Edmond-s-Algorithm.git
pip install networkx
pip install matplotlib

cd src

Commands:

Custom graph:
python3 main.py custom_input_graph minimum root="a" < input.txt

Default graph:
python3 main.py
python3 main.py maximum

To sketch a graph, simply include "sketch" flag anywhere in the args.
For example, python3 main.py sketch --> will sketch Minimum Spanning Tree of the default graph.

Python version: 3.8.9 on a 64-bit machine running on MacOS Monterey v 12.3.1

