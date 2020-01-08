from functools import reduce
def is_palindrome(num):
    s1 = str(num)
    # return s1 == s1[::-1]
    return s1 == reduce(lambda x,y:y+x,s1)
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))