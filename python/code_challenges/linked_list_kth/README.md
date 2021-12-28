# 7 Linked List kth position

[Recent PR](https://github.com/idcargill/data-structures-and-algorithms/pull/29)

## Project Summary

To find the kth value of a linked list I iterated through the linked list with 2 pointers both starting at the head. The first pointer moved through the list, the second waited until it was 'k' nodes behind the first, then iterated through. When the first pointer reached the end of the list the value of pointer 2 is returned.

### Whiteboard

![kth_from_end.png](kth_from_end.png)
