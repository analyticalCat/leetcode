#given a string, determine if a permutation of the string could form a palindrome

class Solution:
    def palindromePermutation(self, str1):
        char_set = set()
        for ele in str1:
            if ele in char_set:
                char_set.remove(ele)
            else:
                char_set.add(ele)
        return len(char_set)<=1



obj = Solution()
print(obj.palindromePermutation('test12321test'))