import os
first = input()
second = input()
if os.path.exists(first):
    src, dst = first, second
else:
    src, dst = second, first
with open(src, encoding="utf-8") as f:
    nums = [int(line) for line in f if line.strip()]
with open(dst, "w", encoding="utf-8") as f:
    f.write(str(nums[-1]) + "\n")
    f.write(str(nums[0]) + "\n")
