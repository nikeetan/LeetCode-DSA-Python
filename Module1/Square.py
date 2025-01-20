def bin_mod_sq(x:int):
    if x==0 or x==1:
        return x
    else:
        low = 2
        high = x//2
        while low<=high:
            mid = low+(high-low)//2
            square =mid*mid
            if square == x:
                return mid
            elif square > x :
                high= mid-1
            else:
                res=mid
                low = mid+1
        return res

x = 25
print(bin_mod_sq(x))