# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def summa(nums, target):
    for a in range(len(nums)):
        for b in range(a+1, len(nums)):
            if nums[a] + nums[b] == target:
                return [a, b]


print(summa([1, 2, 5, 8], 9))
print(summa([0, 98, 78, 1, 7], 99))
