with open('input.txt') as fp:
    nums = [int(num) for num in fp.read().splitlines()]


def find_pair(nums, target=2020):
    seen = set()
    for item in nums:
        if (target - item) in seen:
            return item * (target - item)
        seen.add(item)


for idx, num in enumerate(nums[25:]):
    if not find_pair(nums[idx:idx + 25], num):
        target = num
print(target)

size = 2
while True:
    for i in range(len(nums[:idx - size])):
        group = nums[i:i + size]
        if sum(group) == target:
            print(group)
            break
    size += 1

