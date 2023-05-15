# we need range between 1(always starting from 1) and max p in piles. To get it, we initialise binary search, more precisely l,r pointers
l, r  = 0, max(piles)
# it's strange, but we set res to r, cause at least it's gonna work 
res = r
while l <= r:
    k = (r+l)//2 
    # next we initialise hours counter to find minimum and compare it with h input
    hours = 0
    for p in piles:
        hours += math.ceil(p/k)
    
    if hours <= h:
        res =min(res, k)
        r = k - 1
    else:
        l = k + 1
return res