def fun(n):
    if n==0:
        return ""
    else:
        print(n,fun(n-1))
    return "" 
fun(100)
