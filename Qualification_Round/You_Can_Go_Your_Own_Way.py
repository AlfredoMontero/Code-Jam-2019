#!/usr/bin/env python
# coding: utf-8

def get_path(s):
    s = s.replace('S','N')
    s = s.replace('E','S')
    s = s.replace('N','E')
    return s
    

t = int(input()) 
for i in range(t):
    n = int(input())
    s = str(input())
    s = get_path(s)
    print("Case #{}: {}".format(i+1, s))

