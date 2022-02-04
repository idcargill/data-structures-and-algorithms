# Tree Breadth First

- Write a function called breadth first
- Arguments: tree
- Return: list of all values in the tree, in the order they were encountered

NOTE: Traverse the input tree using a Breadth-first approach

## Whiteboard Process

![whiteboard](tree_breadth_first.png)

## Approach & Efficiency

The tree is traversed with each level entered into a queue.
The entire tree must be traversed and is performed in O(n)

## Solution
<!-- Show how to run your code, and examples of it in action -->

```python

from tree_breadth_first.tree_breadth_first import breadth_first
Tree  # loaded tree

breadth_first(Tree)
# [ 2, 7, 5, 6 ...]


```