## ed2-files
This repository consist in all implementations of the data structures seen at UECE'S course of advanced data structures ministered by professor Marcos Negreiros. 
The goal of this project is that be used like material study. 

## Current Data Structures
* Hashing ( Linear Probing, Quadratic Probing, Double Hash and hash with linked list)
* Basic Binary search tree with display in shell

## Basic use example

* Hashing
```
In [1]: from src.hashing.hash_table import HashTable
In [2]: ht = ht = HashTable(size_table=11)
In [3]: ht.bulk_insert([17, 89, 90, 66, 56, 78, 43])
step 1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[None, None, None, None, None, None, 17, None, None, None, None]
step 2
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[None, 89, None, None, None, None, 17, None, None, None, None]
step 3
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[None, 89, 90, None, None, None, 17, None, None, None, None]
step 4
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[66, 89, 90, None, None, None, 17, None, None, None, None]
step 5
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[66, 89, 90, 56, None, None, 17, None, None, None, None]
step 6
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[66, 89, 90, 56, 78, None, 17, None, None, None, None]
step 7
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[66, 89, 90, 56, 78, None, 17, None, None, None, 43]
In [4]: ht.keys()
In [5]: {0: 66, 1: 89, 2: 90, 3: 56, 4: 78, 6: 17, 10: 43}
```
* Binary Search Tree ( Without balancing yet)
```
In [1] : from src.avl_tree.avl import AvlTree
In [2] : tree = AvlTree()
In [3] : tree.bulk_insert([56, 73, 21, 80, 43, 21])
In [4] : tree.display()
   ___56
 /      \
21       73
  \        \
   43       80
   ```





