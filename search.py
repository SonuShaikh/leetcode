# lenear and binary search
class searchingAlgo:

    def __init__(self):
        nums    = [1,3,5,7,9,11,13,15,17,19,21,27]
        target  = 27

        result = self.binary_search(nums, target)

        if result == -1:
            print('Value not found')
        else:
            print(f'The {target} found at index {result}')
    
    def linear_search(self, nums, target):
        for indx, num in enumerate(nums):
            if num == target:
                return indx
        return -1
    
    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
obj = searchingAlgo()