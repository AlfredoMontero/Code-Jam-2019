#!/usr/bin/env python
# coding: utf-8

# In[45]:


def solve1(n):
    l = len(bin(n-1).lstrip('0b'))
    inp = [''] * l
    for i in range(n):
        a = bin(i).lstrip('0b').zfill(n)
        for j in range(l):
            inp[j] += a[n-j-1]
    
    return inp , l

def solve2(m,l):
    a = [''] * len(m[0])
    p = []
    for i in range(len(m[0])):
        for j in range(l):
            a[i] += m[l-j-1][i]
    for k in a:
        p.append(int(k,2))
    return p

def get_values(n,a,b):
    sol = []
    for i in range(n):
        if i not in a:
            sol.append(i)
            b -= 1
            if b == 0:
                break
    return sol

def solve():
    m = []
    n, b, f = map(int, input().split())
    inp , l = solve1(n)
    for i in range(l):
        print(inp[i] , flush = True)
        m.append(str(input()))
    p = solve2(m,l)
    sol = get_values(n,p,b)
    print(*sol , flush = True)
    verdict = int(input())
t = int(input()) 

for _ in range(t):
    solve()

