class Solution:
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
    '''
    def prime(self,num):
        if num < 2:
            return False
        if num == 2 or num == 3:
            return True
        if num % 2 == 0:
            return False    
        divisor = 3
        while divisor * divisor <= num:
            if num % divisor == 0:
                return False
            divisor += 2
        return True
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prev_prime = -1
        min_diff = float('inf')
        to_return = [-1, -1]

        for i in range(left, right + 1):
            if self.prime(i):
                if prev_prime != -1:
                    current_diff = i - prev_prime
                    if current_diff < min_diff:
                        min_diff = current_diff
                        to_return = [prev_prime, i]
                    if current_diff == 1 or current_diff == 2:
                        return [prev_prime,i]
                prev_prime = i
        return to_return





    
        