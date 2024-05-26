class lambda_demo:
    def __init__(self,data:int):
        self.x=data
    #Normal function
    def Normal_function(self):
        return self.x*5
function_demo=lambda_demo(5)
print("From Normal Function:",function_demo.Normal_function())
lambda_function=lambda x : x*5
print("From Lambda Function:",lambda_function(5))

lambda_function1=lambda x,y : x+y
print(lambda_function1(2,3))

