class Pascal:
    def Particular_element(self,row:int,col:int):
        if col>row:
            return "Please Provide the valid column number to fetch the element"
        else:
            row-=1
            col-=1
            numerator=1
            denominator=1
            to_traverse=col
            for i in range(to_traverse):
                numerator*=row
                denominator*=col
                row-=1
                col-=1
            return (numerator//denominator)
    #o(n2) got reduced to o(n)
    # def fetch_Row(self,row:int):
    #     col=1
    #     row_list=[]
    #     while col<=row:
    #         row_list.append(self.Particular_element(row,col))
    #         col+=1
    #     return row_list
    def fetch_Row(self,row:int):
        ans=1
        row_list=[]
        row_list.append(ans)
        
        for i in range(1,row):
            ans=ans*(row-i)
            ans=ans//i
            row_list.append(ans)
        return row_list
    def Print_pascal(self,row:int):
        
        for i in range(1,row+1):
            print(*self.fetch_Row(i))

P=Pascal()
while True:
    print("**********Menu***********")
    print("1. Nth element in a row")
    print("2. Find the Nth row of a Triangle")
    print("3. Print the Pascal's Triangle")
    print("0. For Exit")
    choice=int(input())
    if choice==1:
        row=int(input("Please Enter the Row Number"))
        col=int(input("Please Enter the column Number"))
        print(P.Particular_element(row,col))
    if choice==2:
        row=int(input("Please Enter the row number to fetch")) 
        print(P.fetch_Row(row))
    if choice==3:
        row=int(input("Please input the height of the pascal's Tree:"))
        P.Print_pascal(row)
    if choice==0:
        print("Thank you")
        break
    


