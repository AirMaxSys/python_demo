#!/usr/bin/paython3
# Insertion sort

def insertion(a):
    for listIdx in range( len(a) ):
        for insIdx in range( len( a[:listIdx] ) ):
            if(a[listIdx] < a[insIdx]):
                a.insert(insIdx, a.pop(listIdx))

a = [-1, 100, 12, 15, 1, 50, 25, 16, 13, 56, 11]
insertion(a)
print("Insertion sort: a[] = ", a)