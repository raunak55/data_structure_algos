class Solution():
   def twoSum(self, nums, target):
      """
      :type nums: List[int]
      :type target: int
      :rtype: List[int]
      """
      required = {}
      for i in range(len(nums)):
         print(target - nums[i])
         if target - nums[i] in required:
            #print('*********')
            #print(target - nums[i])
            return [required[target - nums[i]],i]
         else:
            required[nums[i]]=i
         print('^^^^^^^')
         print(required)
input_list = [2,8,12,15]
ob1 = Solution()
print(ob1.twoSum(input_list, 20))