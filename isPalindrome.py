# Palindrome number
# https://leetcode.com/problems/palindrome-number/description/

# Aproch 1
def isPalindrom(num):

    original_number = num
    reverse_number = 0
    # negative number never be a polindrome
    if num < 0: return False

    while num > 0 :
        # fetch last digit
        last_digit = num % 10
        # add the last digit to existing reverse number
        reverse_number = reverse_number * 10 + last_digit
        # remove the last digit from origin number
        num //= 10

    return original_number == reverse_number

print(isPalindrom(1234567))
print(isPalindrom(121))


# Aproch 2
# Above methods check each and every digit even if it's not polindrome
# Which leads to performance issue. 
# 