#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools


def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]


def grouper(iterable, n):
    it = iter(iterable)
    while True:
       chunk = tuple(itertools.islice(it, n))
       if not chunk:
           return
       yield chunk

for x in grouper(open('text'), 10):
    print(x)
# for x in batch(range(0, 10), 3):
#     print(x)
