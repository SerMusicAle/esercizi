"""
    Dato il nodo di testa di una lista concatenata singolarmente, 
        - restituisci true se è un palindromo. 
        - Modella i concetti di Nodo e Lista Concatenata utilizzando classi.

"""

class Node:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self, numeri:list):
        self.numeri = [1,2,3,2,1]



    def is_palindrome(head:Node) -> list[int]:
        for i in len(LinkedList.numeri)//2:
            if i == -i:
                return True
            
LinkedLIst()