lines = [int(num) for num in '7,14,0,17,11,1,2'.split(',')]

from collections import defaultdict

def one(lines):
    nums = defaultdict(list)
    for idx, num in enumerate(lines, start=1):
        nums[num].append(idx)

    last_num = 6
    was_first = True

    for year in range(len(nums)+1, 30000001):
        if was_first:
            num = 0
        else:
            years = nums[last_num]
            num = abs(years[-1] - years[-2])

        nums[num].append(year)
        was_first = len(nums[num]) == 1
        last_num = num

    return last_num


def two(lines):
    pass


print(one(lines))
print(two(lines))
