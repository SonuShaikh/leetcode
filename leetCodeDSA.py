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
        
        
