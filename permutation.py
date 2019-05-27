# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution:
    #def permute(self, nums: List[int]) -> List[List[int]]:
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]

        result =[]
        for i in range(len(nums)):
            temp = self.permute(nums[:i] + nums[i+1:])
            if temp != None:
                for elem in temp: 
                    result.append([nums[i]] + elem) 
        
        return result



class Solution2:  #heap solution.  slower than the solution above, but interesting way to solve the permutation problem
    def permute(self, nums):
        if len(nums)<=1: return [nums]

        result =[]
        self.heapPermute(nums, len(nums), result)
        return result

        
    def heapPermute(self, hnums, size, result):
        if size == 1: 
            result.append(hnums[:])  # not sure why hnums needs to add [:]
        size_down = size - 1
        size_odd = size % 2 == 1

        for i in range(size):
            self.heapPermute(hnums, size_down, result)

            if size_odd:
                if 0 != size_down:
                    hnums[0], hnums[size_down] = hnums[size_down], hnums[0]
            else:
                if i != size_down:
                    hnums[i], hnums[size_down] = hnums[size_down], hnums[i]




# given n = 1,2,...9, and k = 1,2,... n!  return the kth permutation of n.

class Solution3:
    def getPermutation(self, n: int, k: int) -> str:      
        nums =  list(range(1, n+1))
        results = self.permute(nums,k,n)
        return ''.join(str(i) for i in results[k-1])


    def permute(self, nums, k, n):
        if len(nums) <= 1:
            return [nums]

        result =[]
        for i in range(len(nums)):

            temp = self.permute(nums[:i] + nums[i+1:],k, n)

            if temp != None:
                for elem in temp: 
                    result.append([nums[i]] + elem) 

            if len(result) == k:
                if len(result[k-1]) == n:
                    break 
 
                    
        return result
        
#next permutation: 123 ->132, 312->321, 321->123, 132->213, 3142->3214, 31542->
#first, find the last digit which is going up, point to the digit in front of it as the pivot.
#find the largest digit to the right of the pivot and is the furthest one that is > pivot

class Solution4:
    def nextPermutation(self, nums):
        length = len(nums)
        count = length
        succ = 10
        switch = False

        #find the pivot point
        while count>1:
            count -= 1
            if nums[count] >= nums[count -1]: 
                pivot = count - 1
                break

        #find the successor to the right of the pivot
        for i in range(length-1, pivot, -1):
            if nums(i) > nums(pivot) & nums(i)<succ:
                succ = nums(i)


        
                     
        
        
        if not switch:  # completely reverse the list
            nums = nums.reverse

        return nums






obj = Solution4()
print(obj.nextPermutation([1,2,3]))



