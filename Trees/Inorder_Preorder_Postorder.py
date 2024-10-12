# Python3 program for the above approach

# Structure of the
# node of a binary tree
class Node:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None

# Function to print all nodes of a
# binary tree in Preorder, Postorder
# and Inorder using only one stack
def allTraversal(root):
	Preorder=[]
	Inorder=[]
	Postorder=[]
	stack=[]
	stack.append([root,1])
	while len(stack)>0:
		if stack[-1][1]==1:
			node=stack[-1][0]
			Preorder.append(node.data)
			stack[-1][1]+=1
			if node.left:
				stack.append([node.left,1])
		elif stack[-1][1]==2:
			node=stack[-1][0]
			Inorder.append(node.data)
			stack[-1][1]+=1
			if node.right:
				stack.append([node.right,1])
		elif stack[-1][1]==3:
			node=stack[-1][0]
			Postorder.append(node.data)
			stack.pop()
	print("Preorder: ",Preorder)
	print("Inorder: ",Inorder)
	print("Postorder: ",Postorder)

# Driver Code
if __name__ == '__main__':

	# Creating the root
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)

	# Function call
	allTraversal(root)

	# This code is contributed by mohit kumar 29.
