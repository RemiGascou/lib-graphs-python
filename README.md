# Graphs library in Python 3.*

This is a Python 3.* library for implementing graphs

**Requirements : package graphviz**
```python
pip install graphviz
```

## General examples

### Graph creation

Syntax :
```python
g = Graph(listOfNodeLabels=[], listOfEdges=[])
```

where:
- `listOfNodeLabels[]` is a list of strings where each string is the name of a node
- `listOfEdges=[]` is a list of edges where each edges is a list composed of the start node and the and node

`listOfNodeLabels` and `listOfEdges` are optional

You can create a simple graph like this :

```python
g1 = Graph(["a", "b", "c"], [["a", "b"], ["b", "c"], ["c", "a"]])
```


### Nodes

### Edges


## Exporting graphs

You can export a simple graph like this :

```python
g1 = Graph(["a", "b", "c"], [["a", "b"], ["b", "c"], ["c", "a"]])
g1.export("graph.png", fileformat='png')
```

- `fileformat` can be `'png', 'pdf'`
