from functools import lru_cache

with open('input.txt') as fp:
    lines = fp.read().splitlines()
    nums = [int(line) for line in lines]


def one(nums):
    nums.sort()
    diffs = [b - a for a, b in zip([0] + nums, nums + [max(nums) + 3])]
    return diffs.count(1) * diffs.count(3)


@lru_cache()
def two(target):
    if target == 0:
        return 1
    if target not in nums:
        return 0
    else:
        return sum([two(target - 1), two(target - 2), two(target - 3)])


print(one(nums))
nums = set(nums)
print(two(max(nums)))
