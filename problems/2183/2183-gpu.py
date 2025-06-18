import cupy as cp
from data import nums, k

class Solution:
    def countPairs(self, nums, k):
        nums_gpu = cp.array(nums)  # Transfer data to the GPU
        pairs = 0

        for i in range(len(nums_gpu) - 1):
            for j in range(i + 1, len(nums_gpu)):
                ans = nums_gpu[i] * nums_gpu[j]

                if ans % k == 0:
                    pairs += 1
                    print(f'[{i}]: {nums[i]} x [{j}]: {nums[j]} = {ans} - success')
                else:
                    print(f'[{i}]: {nums[i]} x [{j}]: {ans} - failed')

        return pairs

# Example Usage
solution = Solution()
print(solution.countPairs(nums, k))
