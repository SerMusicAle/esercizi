"""
    Dato un array di interi nums e un intero target, restituisci gli indici dei due 
    numeri tali che la loro somma sia uguale a target.

    Puoi assumere che ogni input abbia esattamente una soluzione e non puoi utilizzare 
    lo stesso elemento due volte.

    Puoi restituire la risposta in qualsiasi ordine.    
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
"""

from typing import List, Optional
class Solution(object):
    
    nums: List[int]
    target: int

    def twoSum(self, nums:list[int], target:int) -> Optional[List[int]]:

        i = 0
        while i < len(nums:list):
            l = i+1
            while l < len (nums:list):
                if nums[i] + nums [l] == target:
                    return [i,l]
                l += 1
            i+= 1
            
class Solution2:
    
    nums: List[int]
    target: int
    
    def twoSum (self, nums: list[int], target: int) -> Optional[List[int]]:
        
        num_id = {}
        for i,num in enumerate (nums):
            
            complementare = target - num
            
            if complementare in num_id:
                return [num_id[complementare], i]
            num_id[num] = i
            