
# insertion sort
def threeSum(nums: list[int]):
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[j + 1] < nums[j]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j -= 1

    result = set()

    for i in range(len(nums)):
        target = -nums[i]
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                result.add((-target, nums[left], nums[right]))
                left += 1
                right -= 1
            elif current_sum > target:
                right -= 1
            else:
                left += 1
    return list(result)

print(threeSum([-1, 0, 1, 2, -1, -4]))


# [[-1, -1, 2], [-1, 0 , 1]]



"""
повернути 3 різні між собою числа, які в сумі дають 0

a + b + c = 0
a + b = 0 - c
c = -(a + b) # target
-c = (a + b) # -target
"""


