# Python leetcode two some
# https://leetcode.com/problems/two-sum/

def twoSum(array,target):
    seen_dict = {}
    for indx, num in enumerate(array):
        compliment = target - num
        if compliment in seen_dict:
            return (seen_dict[compliment],indx)
        seen_dict[num] = indx
    
print(twoSum([3,2,4],6))