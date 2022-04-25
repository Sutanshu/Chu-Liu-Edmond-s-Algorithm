# Chu-Liu-Edmond-s-Algorithm

This algorithm is an implementation of the [**Chu-Liu-Edmond**](https://en.wikipedia.org/wiki/Edmonds%27_algorithm) algorithm. It finds the minimum and maximum spanning tree of a directed graph. The running time is ```O(|V|*|E|)``` where |V| is the number of vertices, and |E| is the number of edges. The running time of individual functions is mentioned in the code. 

The file ChuLiuEdmond.py contains the algorithm almost exactly as the wikipedia describes it in English, with helper functions being extracted into a utils folder. 

Steps:
- git clone https://github.com/Sutanshu/Chu-Liu-Edmond-s-Algorithm.git ChuLiuEdmondsProject
- cd ChuLiuEdmondsProject
- pip install networkx
- pip install matplotlib
- cd src

Commands:

Custom graph:
```
python3 main.py custom_input_graph minimum root="a" < input.txt
```

Default graph:
```
python3 main.py
python3 main.py maximum
```

To sketch a graph, simply include "sketch" flag anywhere in the args.
For example, 
```
python3 main.py sketch
``` 
This will sketch Minimum Spanning Tree of the default graph.

To run a sanity test with a random graph:
```python3 adHocSanityTest.py```

Python version: 3.8.9 on a 64-bit machine running on MacOS Monterey v 12.3.1

Author: Sutanshu Seth, 26 April 2022.

