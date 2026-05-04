class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # "indice can be any position" -> i use enumerate to get index 'i'
        for i, n1 in enumerate(nums):
            
            # "i and j must be different" ->  start 'j' from 'i + 1'
            for j in range(i + 1, len(nums)):
                n2 = nums[j]
                
                # "condition : nums[i] + nums[j] == target"
                if n1 + n2 == target:
                    
                    # "indices return ans no value" -> Output list [i, j]
                    return [i, j] # if i used [n1,n2] that return value 