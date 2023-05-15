# we need to initialise res and can set its value to random num in nums
res = nums[0]
# as always, initilise 2 pointers
l, r = 0, len(nums)-1
# as always, using WHILE lOOP:
while l < r:
    # this is the most difficult part to memorize. EDGE CASE(if we get already sorted array, we should update our res and end our execution)
    if nums[l] < nums[r]:
        res = min(res, nums[l])
        break

    # But if it doesn't appeare so, we use binary search. As we know, first we need to find a med nums and update it
    m = (r+l)//2
    res = min(res, nums[m])
    if nums[l] > nums[r]:
        l = m+1
    else:
        r = m-1
return res

