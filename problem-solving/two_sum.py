# Problem: Two Sum
# Approach:
# Time:
# Space:

def two_sum(nums, target):
   
    pass


print(two_sum([2, 7, 11, 15], 9))  # expected: [0, 1]

# Problem: Two Sum

# Time: O(n)
# Space: O(n)

def two_sum(nums, target):
    seen = {}  # number -> tar index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


print(two_sum([2, 7, 11, 15], 9))  # expected: [0, 1]

