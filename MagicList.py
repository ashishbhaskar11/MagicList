class MagicList :
	def __init__(self):
		self.data = [0]
	
	def findMin(self):
		M = self.data
		''' you need to find and return the smallest
			element in MagicList M.
			Write your code after this comment.
		'''
		if len(M)==1:
			return None
		else:
			return M[1] #it can be easily understood that the minimum element will always be the element at the index 1


	def insert(self, E):
		M = self.data
		''' you need to insert E in MagicList M, so that
			properties of the MagicList are satisfied. 
			Return M after inserting E into M.
			Write your code after this comment.
		'''
		M.append(E)
		for i in range(len(M)-1,0,-1): #starting comparison from the last element
			if M[i//2] > M[i]:  #comparing the child and the parent, if parent is greater we will swap the parent with its children
				M[i//2] , M[i] = M[i] , M[i//2]
			else:
				continue  	
		return M

	def deleteMin(self):
		M = self.data
		''' you need to delete the minimum element in
			MagicList M, so that properties of the MagicList
			are satisfied. Return M after deleting the 
			minimum element.
			Write your code after this comment.
		'''
		if len(M)==1:
			return M
		else:
			M[1] , M[-1] = M[-1] , M[1]   # swaping the min. element and the last element
			M.pop()  #deleting the min. element which was at the last position
			
			for i in range(len(M)):
				if M[i//2] > M[i]:   #from the first element onwards we start comparing the element with its children and if parent is larger we will swap them
					M[i//2] , M[i] = M[i] , M[i//2]
				else:
					continue 
		return M


def K_sum(L, K):
	''' you need to find the sum of smallest K elements
		of L using a MagicList. Return the sum.
		Write your code after this comment.
	'''
	M=MagicList()
	for i in L:  #first we will form a magiclist with all the elements of L
		M.insert(i)
		
	sum=0 #to keep the track of sum of the elements we take a variable sum and initailize it with 0
	index=0
	while index<K:
		index+=1
		sum = sum + M.findMin()   # we will add the value of minimum magic element in sum and then delete 
		M.deleteMin()	# the that element so that next time when we itterate it will fetch the next
	return sum	        # minimum element and that's why we are deleting the minimum element
	
	
if __name__ == "__main__" :
	'''Here are a few test cases'''
	
	'''insert and findMin'''
	M = MagicList()
	M.insert(4)
	M.insert(3)
	M.insert(5)

	x = M.findMin()
	if x == 3 :
		print("testcase 1 : Passed")
	else :
		print("testcase 1 : Failed")
		
	'''deleteMin and findMin'''
	M.deleteMin()
	x = M.findMin()

	if x == 4 :
		print("testcase 2 : Passed")
	else :
		print("testcase 2 : Failed")
		
	'''k-sum'''
	L = [2,5,8,3,6,1,0,9,4]
	K = 4
	x = K_sum(L,K)
	if x == 6 :
		print("testcase 3 : Passed")
	else :
		print("testcase 3 : Failed")