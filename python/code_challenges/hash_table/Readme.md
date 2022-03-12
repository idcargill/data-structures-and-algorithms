# Hash Table

[challenge-30](https://canvas.instructure.com/courses/3826570/assignments/26339206?return_to=https%3A%2F%2Fcanvas.instructure.com%2Fcalendar%23view_name%3Dmonth%26view_start%3D2022-03-12)

## Challenge

Implement hash map functionality for the following methods. 

- hash
- contains
- get
- set
- keys

## Approach & Efficiency

Implemented a HashTable class with a list of None values. Items are added to the hash storage as lists. Collisions are appended to the bucketed list.

## API

h = HashTable()

- h.get(key): returns value

- h.contains(key): returns bool

- h.set(key, value): void

- h.keys(): returns a list of sorted keys
