"""
    dati due array di interi nums1 e nums2, 
        - ordinati in ordine non decrescente, 
    dati due interi m e n, 
        - rappresentano il numero di elementi in nums1 e nums2 rispettivamente. 
    Scrivi una funzione per unire nums1 e nums2 in un singolo array ordinato in ordine non decrescente.

    L'array ordinato deve essere memorizzato all'interno dell'array nums1. 
        - nums1 ha una lunghezza di m + n, 
        - i primi m elementi indicano gli elementi che devono essere uniti, 
        - gli ultimi n elementi sono impostati su 0 e devono essere ignorati. 
        - nums2 ha una lunghezza di n.

"""


def merge(nums1, m, nums2, n):
    
    #_INIT
    


    #BODY  
    nums1[:] = [num for num in nums1 if num !=0]
    nums2[:] = [num for num in nums2 if num !=0]
    
    nums1[m:] = nums2
    
    nums1.sort()
    #RETURN
  
    return (nums1)

