from typing import List


# 二分查找法
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # 从候选值中返回结果,left+1=right
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
