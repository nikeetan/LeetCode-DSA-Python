class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0]*len(code)
        elif k>0:
            to_divide=len(code)
            new_list=[0]*to_divide
            i=0
            while i<to_divide:
                j=i+1
                sum1=0
                print('for i th pos',i)
                while j<k+i+1:
                    sum1+=code[j%to_divide]
                    print(code[j%to_divide])
                    j+=1
                new_list[i]=sum1
                i+=1
            return new_list
        else:
            to_divide=len(code)
            new_list=[0]*to_divide
            i=0
            while i<to_divide:
                j=i-1
                sum1=0
                while j>k+i-1:
                    sum1+=code[j%to_divide]
                    j-=1
                new_list[i]=sum1
                i+=1
            return new_list

    
        