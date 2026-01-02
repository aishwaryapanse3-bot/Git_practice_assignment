# 1. Find the sum of all elements in a list 
# Input: [1, 2, 3, 4]  Output: 10

nums = [1,2,3,4]
print(sum(nums))

# 2. Find the largest and smallest element 
# Input: [4, 1, 9, 2] Output: Max = 9, Min = 1

nums = [4,1,9,2]
print("max= ", max(nums))
print("min= ",min(nums))

# 3. Count even and odd numbers
# Input: [1, 2, 3, 4, 5, 6] Output: Even = 3, Odd = 3

nums = [1,2,3,4,5,6]
even = 0
odd = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print("even= ", even)
print("odd= ",odd)

#4. Reverse a list (without using reverse())
# Input: [1, 2, 3] Output: [3, 2, 1]

nums = [1, 2, 3]
print(nums[::-1])

# 5. Check if list is empty 
# Input: [] Output: True

nums = []

if nums == []:
    print(True)
else:
    print(False)

