#!/usr/bin/env python
# -*- coding: utf-8 -*-


def f(y):
    x = yield y
    yield x
    x = yield y
    yield x

gen = f(0)

next(gen)
print(gen.send(1))
print(next(gen))
print(gen.send(2))
print(next(gen))
