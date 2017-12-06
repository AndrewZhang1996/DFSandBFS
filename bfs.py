class bfs():

	def __init__(self,vertices,start):
		self.vertices=vertices
		self.start=self.get_vertice(start)
		self.visit=[0]*len(self.vertices)
		self.algorithm()

	def get_vertice(self,name):
		for vertice in self.vertices:
			if vertice.name==name:
				return vertice

	def algorithm(self):
		print("**************************This is the DFS algorithm***********************")
		self.bfs_procedure(self.start) # 8n+3
		for vertice in self.vertices: # n
			if self.visit[self.vertices.index(vertice)]==0:
				self.bfs_procedure(vertice)
		print("**************************************************************************")

	def bfs_procedure(self,vertice): # 8n+3
		queue = [] # 1
		self.visit[self.vertices.index(vertice)] = 1 # 1
		queue.insert(0,vertice) # 1
		print vertice.name+'--->', # 1

		while len(queue)!=0: # n + 1
			
			vertice_1=queue.pop() # n
			vertice_2=self.get_unvisited_linked_vertice(vertice_1) # n
			while vertice_2!=None: # n
				self.visit[self.vertices.index(vertice_2)]=1 # n-1
				print vertice_2.name+"--->", # n-1
				queue.insert(0,vertice_2) # n-1
				vertice_2=self.get_unvisited_linked_vertice(vertice_1) # n-1
		print("end") # 1
		print str(count) # 1

	def get_unvisited_linked_vertice(self,vertice):
		v=None
		for linked_vertice in vertice.linked_vertices:
			if self.visit[self.vertices.index(linked_vertice['vertice'])]==0:
				v=linked_vertice['vertice']
				break
		return v


	






