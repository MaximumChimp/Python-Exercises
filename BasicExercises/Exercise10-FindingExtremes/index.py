#PROBLEM : Given a list of integers, find and print both the largest and the smallest numbers.
#PURPOSE : This exercise explores “Aggregate Functions.” While Python has built-in tools for this, understanding how to identify extremes is critical for data normalization, where you often need to find the range of a dataset before processing it.

nums = [45,2,89,12,7]

#SOLUTION 1
print(f'Largest: {max(nums)} Smallest: {min(nums)}')

#SOLUTION 2
temp = nums[0]
print(f"initial: {temp}")
for i in nums:
    if i > temp:
        temp = i
print(temp)