class Solution:
    def bin_search(self,array:List[List[int]],high:int,low:int,target:int,pos:int):
        while low<=high:
            mid=high+(low-high)//2
            if array[mid][0]==target:       
                low=mid+1
            elif array[mid][0]<target:     
                low=mid+1
            else:
                high=mid-1
        return high

        '''
        if array[mid][0]==target:
            pos=mid
            return self.bin_search(array=array,high=high,low=mid+1,target=target,pos=pos)
        elif array[mid][0]<target:
            return self.bin_search(array=array,high=high,low = mid+1,target=target,pos=pos)
        else:
            return self.bin_search(array=array,high=mid-1,low=low,target=target,pos=pos)
        '''

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items=sorted(items)
        maximum={}
        maxi=0
        ele=0
        to_return=[]
        for i in range(len(items)):
            maximum[i]=max(maxi,items[i][-1])
            maxi=max(maxi,items[i][-1])
            high=len(items)-1
            low=0
        for i in queries:
            ele=self.bin_search(array=items,high=high,low=low,target=i,pos=-1)
            if ele in maximum:
                to_return.append(maximum[ele])
            else:
                to_return.append(0)
        return to_return