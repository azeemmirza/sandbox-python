from data import nums, k

class Solution:
    def countPairs(self, nums, k):
        pairs = 0
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                ans = nums[i] * nums[j]

                if ans % k == 0:
                    pairs += 1
                    print(f'[{i}]: {nums[i]} x [{j}]: {nums[j]} = {ans} - success')
                else:
                  print(f'[{i}]: {nums[i]} x [{j}]: {nums[j]} = {ans} - failed')
        
        return pairs

solution = Solution()
print(len(nums))
print(solution.countPairs(nums, k))