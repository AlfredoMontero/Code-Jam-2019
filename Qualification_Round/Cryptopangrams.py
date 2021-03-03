#!/usr/bin/env python
# coding: utf-8

# In[108]:


def gcd(a, b):
    if b == 0: 
        return a
    return gcd(b, a%b)

def decipher(l):
    k = 1
    for i in range(len(l)-1):
        if l[i] != l[i+1]:
            b = gcd(l[i],l[i+1])
            break
        else:
            k += 1
    
    a = [None] * k
    a.append(b)
    for i in range(1,k+1):
        a[k-i] = l[k-i] // a[k-i+1]
    for i in range(k+1,len(l)+1):
        a.append(l[i-1] // a[i-1])
    c = sorted(set(a))
    return c , a

def get_code(letters , l1 , l2):
    dic = dict(zip(l1,letters))
    st = ''
    for i in l2:
        st += dic[i]
    return(st)

letters = list(map(chr, range(65, 91)))
t = int(input()) 
for i in range(t):
    n , le = [int(s) for s in input().split(" ")]
    lst2 = list(input().split())
    lst = list(map(int, lst2))
    l1 , l2 = decipher(lst)
    s = get_code(letters , l1, l2)
    print("Case #{}: {}".format(i+1, s))

