import numpy as np
class dijkstra_queue():
	global INF
	INF = 32767

	def __init__(self, digraph):
		self.digraph_vertices = digraph.get_vertices()
		self.vertices_paths = []
		self.any_two_arbitrary_vertices()

	def any_two_arbitrary_vertices(self):
		for vertice in self.digraph_vertices:
			shortest_paths = self.get_shortest_path(vertice)
			vertice_paths = {'start_vertice':vertice,'shortest_paths':shortest_paths}
			self.vertices_paths.append(vertice_paths)
		filename = 'dijkstra_queue.npy'
		np.save(filename,self.vertices_paths)
					

	def get_shortest_path(self,start):
		shortest_paths=[]
		shortest_distance=0
		path=[]
		vertice_path=[]
		start_index=self.digraph_vertices.index(start)
		dis,shortest_path=self.algorithm(start)
		print(shortest_path)
		for vertice in self.digraph_vertices:
			shortest_path={}
			if vertice!=start:
				end_index=self.digraph_vertices.index(vertice)
				t=end_index
				while t!=start_index:
					path.append(t)
					t=shortest_path[t]
				path.append(t)
				path.reverse()
				for index in path:
					vertice_path.append(self.digraph_vertices[index])
				shortest_path={'end_vertice': self.digraph_vertices[end_index] ,'path':vertice_path,'distance':shortest_distance}
				shortest_paths.append(shortest_path)
		return shortest_paths

	def get_distance_between_two_linked_vertices(self,start,end):
		distance = INF
		for vertice in start.linked_vertices:
			if vertice['vertice']==end:
				distance=vertice['length']
		return int(distance)

	def algorithm(self, start):
		vertices_num = len(self.digraph_vertices)
		shortest_path = [0]*vertices_num
		visit = [0]*vertices_num
		distance = [INF]*vertices_num

		distance[self.digraph_vertices.index(start)] = 0

		for j in range(0,vertices_num):
			min_vertice = None
			min_position = -1
			temp_shortest_distance = INF

			for i in range(0,vertices_num):
				vertice = self.digraph_vertices[i]
				if visit[i]==0 and distance[i]<temp_shortest_distance:
					min_vertice = vertice
					min_position = i
					temp_shortest_distance = distance[i]
			visit[min_position] = 1

			for i in range(0,vertices_num):
				vertice = self.digraph_vertices[i]
				if visit[i]==0 and int(distance[min_position])+self.get_distance_between_two_linked_vertices(min_vertice,vertice)<distance[i]:
					distance[i] = int(distance[min_position])+self.get_distance_between_two_linked_vertices(min_vertice,vertice)
					shortest_path[i] = min_position
		return distance, shortest_path

		