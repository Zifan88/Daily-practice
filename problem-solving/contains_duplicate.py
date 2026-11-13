# Problem: Contains Duplicate
# Approach: Set e ager dekha number rakhi. Notun number ager theke set e thakle duplicate paoa gelo.
# Time: O(n)
# Space: O(n)

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


print(contains_duplicate([1, 2, 3, 1]))  # True
print(contains_duplicate([1, 2, 3, 4]))  # False
print(contains_duplicate([]))            # False