import random
nums= []
def find_missing_nums(nums):
n= int(input())
for i in range(n):
I = random.randint(1, n)
nums.append(I)
return (nums)
print(find_missing_nums(nums))