class Solution:
    '''
    sieve of eratosthenes
    '''
    def prime(self,left,right):
        list1=[True for i in range(right+1)]
        list1[0]=list1[1]=False
        start=2
        primel=[]
        while start*start<=right:
            if list1[start]:
                for i in range(start*start,right+1,start):
                    list1[i]=False
            start+=1
        for i in range(left,right+1):
            if list1[i]:
                primel.append(i)
        return primel

    def closestPrimes(self, left: int, right: int) -> List[int]:
        list_prime=[]
        l=self.prime(left,right)
        min_gap=float('inf')
        p1,p2=0,1
        to_return=[]
        while p2<len(l):
            if l[p2]-l[p1]<min_gap:
                min_gap=l[p2]-l[p1]
                to_return=[]
                to_return.extend([l[p1],l[p2]])
            p1+=1
            p2+=1
        return to_return if to_return else [-1,-1]