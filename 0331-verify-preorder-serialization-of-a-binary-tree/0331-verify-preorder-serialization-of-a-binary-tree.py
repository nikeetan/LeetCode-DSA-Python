'''
inorder i have always  # node.val # 
preorder i have node.val, #, #, node.val it would atleast 2 hashes and then followed node


i have  a node after that if i have 2 hashes then that's the leaf node i should be able to find the prev node from the curr node and then attach the next element if i don't have that then it's not the valid preorder


9 #  # 1
i can think of using stck here the moement i encounter two hash i will pop top of the stk
after that i will be having one two_hashconts = 1

the movement i reach  2 hash i will start poping
if two 2 hash counts then pop
if 1 two hash counts and 1 hash count then also pop 

each valid nod produces two slots and consumes one slots
'''



class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        preorder = preorder.split(",")
        for i in preorder:
            if slots <= 0:
                return False
            if i != '#':
                slots += 1
            elif i == '#':
                slots -= 1
        return slots == 0

