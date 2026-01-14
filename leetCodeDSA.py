# Find max number by changing single digit in given number
# https://leetcode.com/problems/maximum-69-number

class Solution:
    def maximum69Number (self, num: int) -> int:
        numArray = []
        
        # handle if zero is number (which will not be the case here)
        if num == 0:
            return 9

        # conversion of number to array
        while(num > 0):
            numArray.insert(0, num % 10) # Insert last element
            num //= 10 # Remove last element

        for i in range(len(numArray)):
            if numArray[i] != 9:
                numArray[i] = 9
                break
        
        new_num = 0
        for digit in numArray:
            new_num = new_num * 10 + digit
        
        return new_num

        #return int(''.join(map(str,numArray)))

# https://leetcode.com/problems/remove-duplicates-from-sorted-array
# remove duplicate from sorted array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Handle if no records present
        if not nums:
            return 0

        # first element always be unique
        i = 0

        # start second pointer from 1 position
        for j in range(1, len(nums)):
            # if value of J and I is not matching
            # then new unique element
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1 