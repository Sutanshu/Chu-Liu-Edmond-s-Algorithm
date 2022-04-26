# Chu-Liu-Edmond-s-Algorithm

This algorithm is an implementation of the [**Chu-Liu-Edmond**](https://en.wikipedia.org/wiki/Edmonds%27_algorithm) algorithm. It finds the minimum and maximum spanning tree of a directed graph. The running time is ```O(|V|*|E|)``` where |V| is the number of vertices, and |E| is the number of edges. The running time of individual functions is mentioned in the code. 

The file ChuLiuEdmond.py contains the algorithm almost exactly as the wikipedia describes it in English, with helper functions being extracted into a utils folder. 

# Assumptions made:
- The graph is connected.
- The root node has no incoming node

# Steps:
- git clone https://github.com/Sutanshu/Chu-Liu-Edmond-s-Algorithm.git ChuLiuEdmondsProject
- cd ChuLiuEdmondsProject
- pip install networkx
- pip install matplotlib
- cd src

# Commands:

Please note that the position of the "root" flag must be as is.

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

# Example run:
```python3 main.py custom_input_graph maximum root="a" < input.txt sketch```

Input graph:
<img width="1118" alt="Screen Shot 2022-04-25 at 5 52 35 PM" src="https://user-images.githubusercontent.com/42788023/165192689-ad4cd81d-8bb5-4b7e-b69a-0de45aab9b32.png">

MaxST my implementation:
<img width="1118" alt="Screen Shot 2022-04-25 at 5 53 13 PM" src="https://user-images.githubusercontent.com/42788023/165192739-954775d5-4bd5-423a-bcae-c2f716725b06.png">

MaxST networkx's implementation:
<img width="1115" alt="Screen Shot 2022-04-25 at 5 52 52 PM" src="https://user-images.githubusercontent.com/42788023/165192707-5431647c-33e7-48f8-83d5-00ca60ae1fa0.png">


Note:
networkx does not comply with my assumptions and works more broadly, and this may cause a few inconsistencies in the output, [**Read here**](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.branchings.Edmonds.html)


Python version: 3.8.9 on a 64-bit machine running on MacOS Monterey v 12.3.1

Author: Sutanshu Seth, 26 April 2022.

