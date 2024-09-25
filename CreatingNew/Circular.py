count=0
array=[1,2,3,4,5,6,7,8,9]
no_of_times=-1
i=0
while no_of_times!=i or count!=2:
    if no_of_times==-1:
        no_of_times=i
        count+=1
    elif no_of_times==i:
        count+=1
        print("")
    print(array[i],end=' ')
    i=(i+1)%len(array)

