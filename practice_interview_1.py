
from nums import LIST_INTS

LIST_INTS = LIST_INTS.split(" ")

def max_int(nums, k):

    highest = []

    for num in nums:
        num = int(num)
        if num % 10 == 3:
            if len(highest) < k:
                highest.append(num)

            else:
                highest = sorted(highest)
                if num > highest[0]:
                    highest[0] = num

    return highest




k = 7

print max_int(LIST_INTS, k)