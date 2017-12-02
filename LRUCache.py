#!/usr/bin/env python
# -*- coding: utf-8 -*-


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.keys = []
        self.cache = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keys:
            return -1
        self.keys.remove(key)
        self.keys.insert(0, key)
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.cache[key] = value
        if key in self.keys:
            self.keys.remove(key)
        self.keys.insert(0, key)
        if len(self.keys) > self.capacity:
            del self.cache[self.keys.pop()]


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    print cache.get(1)
    print cache.get(2)
