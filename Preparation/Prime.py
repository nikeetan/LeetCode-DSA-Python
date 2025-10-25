def sieve_method(n):

    p =  2
    visited = [True] * (n + 1)
    while p * p <= n:
        '''
        why we mark from p * p because the multiples which are lesser than p are already marked by k which is less than p 
        what i meant here was 5 * 5 = 25 but 10, 15 , 20 will be derived by multiples of 2  3 which are the lesser than 5 
        '''
        if visited[p]:
            for i in range(p * p, n + 1,  p):
                visited[i] = False
        p += 1
    res = []
    for i in range(2, n + 1):
        if visited[i]:
            res.append(i)
    return res

print(sieve_method(30))



