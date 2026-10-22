name = input()
with open(name, encoding="utf-8") as f:
    nums = [int(line) for line in f if line.strip()]
print(nums[0])
print(nums[1])
print(nums[-2])
print(nums[-1])
