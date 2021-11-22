with open('input.txt') as fp:
    nums = [int(line) for line in fp]


def find_pair(nums, target=2020):
    seen = set()
    for item in nums:
        if (target - item) in seen:
            return item * (target - item)
        seen.add(item)


def find_three(nums, target=2020):
    for idx, item in enumerate(nums):
        if ab := find_pair(nums[:idx], target - item):
            return ab * item


print(find_pair(nums))
print(find_three(nums))
