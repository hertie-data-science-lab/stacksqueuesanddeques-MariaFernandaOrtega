# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:34:20 2023

@author: Maria Fernanda Ortega
"""

from ArrayDeque import Deque

d = Deque()
print(d.items)

for i in range(10):
    d.add_last(i)
    print(d.items)

for i in range(10):
    d.add_first(i)
    print(d.items)

for i in range(10):
    d.delete_last()
    print(d.items)

for i in range(10):
    d.delete_first()
    print(d.items)

for i in range(20):
    d.add_last(i)
    print(d.items)

for i in range(20):
    d.add_first(i)
    print(d.items)

for i in range(20):
    d.delete_last()
    print(d.items)

for i in range(20):
    d.delete_first()
    print(d.items)

d.add_first(20)
print(d.items)

d.add_last(21)
print(d.items)

d.add_first(22)
print(d.items)

d.add_last(23)
print(d.items)

d.add_first(24)
print(d.items)

