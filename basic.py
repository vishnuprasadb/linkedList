class node:
	def __init__(self,data):
		self.data=data
		self.nextNode=None

class linkedList:
	def __init__(self):
		self.head=None

	def printList(self):
		temp=self.head
		while(temp):
			print ("%s"%temp.data,end="")
			temp=temp.nextNode
		print ("")
		
if __name__ == '__main__':

	l = linkedList()

	l.head =node(1)
	second=node(2)
	third=node(3)

	l.head.nextNode=second
	second.nextNode=third

	l.printList()
