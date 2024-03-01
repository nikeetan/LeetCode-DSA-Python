'''
if an array contains the numbers from 1 to n i should find the missing number in an array and the number which has occured more than once 
that is repeating element in an array in o(1) space and o(n) complexity
'''
class Missing:
    def __init__(self,array,n):
        self.array=array
        self.size=n
    def operation(self):
        '''
        Traverse the array and make the visited elements as -1
        '''
        for i in range(self.size):        
            '''
            As we know the array index starts from 0 while we have array from 1 that's the reason we are subtration let's say to fetch 
            the last element
            q1 why they have done index -1 
            ans They are using elements as index of an array to mark the elements of the array as visited because 
            if the elements are repeated they will point to the same index and at that index previously we will have made that element
            has been visited 
            Example: If i have [1,2,2,3,4,5] you can see the element 2 if i take it as index it will point to the same location twice 
            hence we can say that this is the repeated element.

            Now why index-1 I know that the array is has elements inclusive of the range [1,n] and if i do self.array[6] when array sixe =6
            it will throw me the list index out of range error
            '''
            if self.array[abs(self.array[i]-1)]>0:
                self.array[abs(self.array[i]-1)]=-self.array[abs(self.array[i]-1)]
            else:
                print("The Repeated number Element of the Array is: ",abs(self.array[i]))
        '''
        now using the same concept finding the missing element as in my array i have used elements as the index
        in the missing element case there exist one element in the array whose index we can't fetch as the element which is used to fetch the 
        index is not available
        once you reach that position in the sense you will find the element unvisited that is positive just return a i+1 so that you will get the elemet 
        '''
        for i in range(self.size):
            if self.array[i]>0:
              return f"The Missing Element in the array is: {i+1}"




array=[1,2,3,6,4,1]
n=len(array)
print(array)
find=Missing(array,n)
print(find.operation())


