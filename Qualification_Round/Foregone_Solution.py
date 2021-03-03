#!/usr/bin/env python
# coding: utf-8

def div_four(n):
    m = str(n)
    l = len(m)
    a = ''
    b = ''
    for k in range(l):
        if int(m[k]) == 4:
            a += '2'
            b += '2'
        else:
            a += '0'
            b += m[k]
            
    return int(a), int(b)
    

t = int(input()) 
for i in range(t):
    n = int(input())
    a , b = div_four(n)
    print("Case #{}: {} {}".format(i+1, a, b))

