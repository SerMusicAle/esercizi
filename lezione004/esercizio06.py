"""
senza usare i set tornare una nuova lista con gli elementi in comune tra le due liste
"""

def intersection (nums1: list[int], nums2: list[int]) ->list[int]:
    lista: list = []
    for i in nums1:
        for l in nums2:
            if i==l and i not in lista:
                lista.append(i)
    return (lista)
res = intersection ([1,2,3,4],[2,2,5,6])
print (res)