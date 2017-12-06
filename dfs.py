class dfs():

	def __init__(self,vertices,start):
		self.vertices = vertices
		self.start = self.get_vertice(start)
		self.visit=[0]*len(self.vertices)
		self.algorithm()

	def get_vertice(self,name):
		for vertice in self.vertices:
			if vertice.name==name:
				return vertice

	def algorithm(self):
		print("**************************This is the DFS algorithm***********************") # 1
		self.dfs_procedure(self.start) # 10n-1
		for vertice in self.vertices: # n-1
			if self.visit[self.vertices.index(vertice)]==0:
				self.dfs_procedure(vertice)
		print("**************************************************************************")


	def dfs_procedure(self,vertice): # 10n-1
		stack = [] # 1
		self.visit[self.vertices.index(vertice)] = 1 # 1
		stack.append(vertice) # 1
		print vertice.name+'--->', # 1

		while len(stack)!=0: # 2n-1
			next=self.get_unvisited_linked_vertice(stack[len(stack)-1]) # 2n-1
			if next==None: # 2n-1
				stack.pop() # n
			else:
				self.visit[self.vertices.index(next)]=1 # n-1
				print next.name+'--->', # n-1
				stack.append(next) # n-1
		print("end") # 1

	def get_unvisited_linked_vertice(self,vertice):
		v=None
		for linked_vertice in vertice.linked_vertices:
			if self.visit[self.vertices.index(linked_vertice['vertice'])]==0:
				v=linked_vertice['vertice']
				break
		return v















