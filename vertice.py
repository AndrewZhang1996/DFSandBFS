class vertice():

	def __init__(self, name):
		self.name = name
		self.linked_vertices = []

	def add_linked_vertices(self, vertice, length):
		linked_vertice = {'vertice': vertice, 'length':length}
		self.linked_vertices.append(linked_vertice)

	def has_linked_vertice(self, name):
		for vertice in self.linked_vertices:
			if vertice['vertice'].name == name:
				return False
		return True





