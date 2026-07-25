nums = (11, 22, 3, 44, 55, 6, 77, 88, 9)
target = 22

i = 0
while i < len(nums):
    if nums[i] == target:
        print(i)      # prints index of target
        # Optionally break if you only want the first occurrence
        # break
    i += 1            # must happen every iteration

    #break
    nums = (11, 22, 3, 44, 55, 6, 77, 88, 9)
target = 22

i = 0
while i < len(nums):
    if nums[i] == target:
        print(i)
        break         # stop after first match
    i += 1