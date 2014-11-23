#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sorting Algorithms"""


def selection(iterable):
    """Implements the selection sort algorithm
    Args: iterable; an unsorted list
    Returns: iterble as a sorted list
    ex:
    >>> sorters.selection([2,1,3])
    [1,2,3]"""
    srtd = []
    small = 0
    while iterable:
        for i in iterable:
            small = i
            for j in iterable:
                if j <= small:
                    small = j
        srtd.append(small)
        iterable.remove(small)
    iterable = srtd
    return iterable


def quick(iterable):
    """Implements a quick sort algorithm before running the selection sort
    Args: iterable; an unsorted list
    Returns: iterable as a sorted list
    ex:
    >>> sorters.quick([2,1,3])
    [1,2,3]"""
    start = iterable[0]
    end = iterable[-1]
    if start < end:
        pivot = len(iterable) // 2
        new = iterable[0]
        iterable[0] = iterable[-1]
        iterable[-1] = new
        quick(iterable[0:pivot])
        quick(iterable[pivot:-1])
    return selection(iterable)
