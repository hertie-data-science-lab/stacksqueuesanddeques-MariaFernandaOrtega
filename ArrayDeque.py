# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:34:01 2023

@author: Maria Fernanda Ortega
"""

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_first(self, item):
        self.items.insert(0, item)

    def add_last(self, item):
        self.items.append(item)

    def delete_first(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def delete_last(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def first(self):
        if self.is_empty():
            return None
        return self.items[0]

    def last(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def __len__(self):
        return len(self.items)

        
   