# Graphs library in Python 3.*

This is a Python 3.* for implementing graphs

**Requirements : package graphviz**
```python
pip install graphviz
```

## General examples

### Graph creation

Syntax :
```python
g = Graph(listofnodes=[], listofnodes=[])
```

listofnodes and listofnodes are optional

You can create a simple graph like this :

```python
g1 = Graph(["a", "b", "c"], [["a", "b"], ["b", "c"], ["c", "a"]])
```

Let's see three equivalent examples :

**Example 1**
```python
g1 = Graph()

g1.add_node("a")
g1.add_node("b")
g1.add_node("c")

g1.add_edge("a", "b")
g1.add_edge("b", "c")
g1.add_edge("c", "a")
```

**Example 2**
```python
g1 = Graph(["a", "b", "c"])

g1.add_edge("a", "b")
g1.add_edge("b", "c")
g1.add_edge("c", "a")
```

**Example 3**
```python
g1 = Graph(["a", "b", "c"], [["a", "b"], ["b", "c"], ["c", "a"]])
```


### Nodes

### Edges


## Rendering

You can render a simple graph like this :

```python
g1 = Graph(["a", "b", "c"], [["a", "b"], ["b", "c"], ["c", "a"]])
g1.export("graph.png", fileformat='png')
```
