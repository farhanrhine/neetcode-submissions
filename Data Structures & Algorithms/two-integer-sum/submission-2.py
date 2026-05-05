#============== my best solution ===============================
class Solution:
    def twoSum(self, nums, target):
        storeMap = {}

        for i , n in enumerate(nums):
            diff = target - n

            if diff in storeMap:
                return [storeMap[diff],i]

            storeMap[n] = i # {number : index}
            
# print(twosum_optimized([2,7,11,15],22))
# workflow
# step 1 - (0,2) goes inside enumerate 
# step 2 - 20 = 22-2, and 20 is not in storeMap so , its skip if block and directly store in storeMap {2:0}
# step 3 - (1,7) goes inside enumerate 
# step 4 - 15 = 22-7, and 15 not in storeMap so, its skip the if block and directly store in storeMap {2:0, 7:1}
# step 5 - (2,11) goes inside enumerate 
# step 6 - 11 = 22-11, and 11 not in storeMap so, its skip the if block and directly store in storeMap {2:0, 7:1, 11:2}
# step 7 - (3,15) goes inside enumerate 
# step 8 - 7 = 22-15, boom i found 7 in storeMap so, that means if block trigger and return me [1,3] 