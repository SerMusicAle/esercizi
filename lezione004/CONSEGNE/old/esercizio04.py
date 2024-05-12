"""
    n data una lista nums di elementi, restituire l'elemento che compare più di n/2 volte
"""
"""
#metodo 1 da verificare

def majority_element (nums:list[int]) ->int:
    count=0
    for i in range((len(nums)//2)+1):
        count = 0
        for l in range (i+1, len(nums)):
            if nums[i] == nums[l]:
                count+=1
            if count>len(nums)/2:
                print (f"{nums[i]}, compare {count} volte")
                return nums[i]

majority_element ([5,2,4,6,6,6,5,5,5,5,2,1,4,5,6,7])

"""

"""
#contiamo quante volte compare ciascun elemento
d: dict [int, int] = {}
for i in nums:
    d[i] = nums.count(i)

lenght = len(nums)
for key in d:
    d[key] /= lenght
    if d[key] > 0.5:
        return key
return none 
"""

"""
for i in nums:
    if nums.count(i) > len(nums) /2:
        return i
return None
"""

