import heapq
class Max_profit:
    def __init__(self,array1,array2,array3):
        self.difficulty=array1
        self.profit=array2
        self.workers=array3
    def operation(self):
        '''
        Thought process same group sort 
        profit ,workers
        '''
       
        clubbed=[(self.difficulty[i],self.profit[i]) for i in range(len(self.difficulty))]
        self.workers=sorted(self.workers)
        clubbed=sorted(clubbed)
        profit=0
        count=0
        res=0
        for i in range(len(self.workers)):
            while count<len(difficulty) and clubbed[count][0]<=self.workers[i]:
                profit =max(profit,clubbed[count][1])
                count+=1
            res+=profit
        return res



difficulty=[85,47,57]
profit=[24,66,99]
workers=[40,25,25]

# difficulty=[66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63]
# profit=[66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77]
# workers=[61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16]

fetch_profit=Max_profit(difficulty,profit,workers)
print(fetch_profit.operation())