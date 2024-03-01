
def sub_set(ind,sum,n,store_sub:list,array):
    if ind==n:
        store_sub.append(sum)
        return
    else:
      sub_set(ind+1,sum+array[ind],n,store_sub,array)
      sub_set(ind+1,sum,n,store_sub,array)

array=[3,1,2]
store_sub=[]
n=3 
sum=0
ind=0
sub_set(ind,sum,n,store_sub,array)
print(sorted(store_sub))
