#!/usr/bin/env python
# coding=utf-8


def compare(a,b):
    return cmp(a, b)


def test():
    print(compare(3, 7))


def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('Bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s

