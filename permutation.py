def permutations(nums):
    perms = [[]]
    for num in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm) + 1):
                new_perm = perm[:i] + [num] + perm[i:]
                new_perms.append(new_perm)
        perms = new_perms
    return perms


nums = []

x = int(input("Enter n: "))

while x < 0:
    print("error: Please Enter a valid number!"),
    x = int(input("Enter n: "))

for i in range(1, x + 1):
    nums += permutations(range(1, i + 1))

print(nums, "\n", "count:", len(nums))
