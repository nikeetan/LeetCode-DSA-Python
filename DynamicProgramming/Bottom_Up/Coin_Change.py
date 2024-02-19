#Bottom up approach
class CoinChange:
    def __init__(self,Coin_array,amount):
        self.Coin_Array=Coin_array
        self.Amount=amount
        self.result_array=[0 if x==0 else self.Amount for x in range((self.Amount)+1) ]
    
    def CoinChange_Operation(self):
        for x in range(1,len(self.result_array)):
            count=1
            for coin in self.Coin_Array:
                if x-coin<0:
                    count+=1
                else:
                    self.result_array[x]=min(self.result_array[x-coin]+1,self.result_array[x])
            if count==len(self.Coin_Array):
                self.result_array[x]=-1

        #         if coin <=x:
        #             no_of_ways=x-coin
        #             if self.result_array[no_of_ways]==-1:
        #                 self.result_array[x]=-1
        #             else:
        #                 self.result_array[x]=min(self.result_array[no_of_ways]+1,self.result_array[x])
        #             flag=1
        #     if flag==0 and  self.result_array[x]==amount:
        #         self.result_array[x]=-1
        return self.result_array[amount]

coin_array=[1,2,5]
amount=11
dp_problem=CoinChange(coin_array,amount)
print(dp_problem.CoinChange_Operation())








