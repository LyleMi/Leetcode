#!/usr/bin/env python
# -*- coding: utf-8 -*-


class LRUCache(object):

    class Node(object):

        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.cache = {}
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        n = self.cache.get(key, None)
        if n is None:
            return -1
        self.update(n)
        return n.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        n = self.cache.get(key, None)
        if n is None:
            n = self.Node(key, value)
            self.cache[key] = n
            self.add(n)
            self.count += 1
        else:
            n.value = value
            self.update(n)

        if self.count > self.capacity:
            toDel = self.tail.prev
            self.remove(toDel)
            del self.cache[toDel.key]
            self.count -= 1

    def update(self, node):
        '''
        :type node: Node
        :rtype: void
        move node to first
        '''
        self.remove(node)
        self.add(node)

    def add(self, node):
        '''
        :type node: Node
        :rtype: void
        '''
        after = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = after
        after.prev = node

    def remove(self, node):
        '''
        :type node: Node
        :rtype: void
        '''
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before

if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    print cache.get(1)
    print cache.get(2)
