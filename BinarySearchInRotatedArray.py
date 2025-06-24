# Problem Statement:
# Given a rotated sorted array 'nums' (sorted in ascending order and rotated at an unknown pivot)
# and an integer 'target', return the index of 'target' in 'nums' if it exists, otherwise return -1.
# You must achieve O(log n) runtime complexity.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0  # Initialize the low pointer
        high = len(nums) - 1  # Initialize the high pointer

        while low <= high:
            mid = (low + high) // 2  # Find the middle index

            # Check if the middle element is the target
            if nums[mid] == target:
                return mid  # Target found at mid
            
            # Determine which part is sorted:
            # If the left part is sorted
            if nums[low] <= nums[mid]:
                # Check if target is in the left sorted part
                if nums[low] <= target < nums[mid]:
                    high = mid - 1  # Search in the left half
                else:
                    low = mid + 1  # Search in the right half
            else:
                # If right part is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1  # Search in the right half
                else:
                    high = mid - 1  # Search in the left half
        
        return -1  # Target not found

# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    print("Index of", target1, "in", nums1, "is:", solution.search(nums1, target1))
    # Output: 4

    # Test case 2
    target2 = 3
    print("Index of", target2, "in", nums1, "is:", solution.search(nums1, target2))
    # Output: -1

    # Test case 3
    nums2 = [1]
    target3 = 0
    print("Index of", target3, "in", nums2, "is:", solution.search(nums2, target3))
    # Output: -1