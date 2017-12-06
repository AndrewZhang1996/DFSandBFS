from node import node
from vertice import vertice
from random import randint as rd

class digraph():

	def __init__(self, number_of_node, upper_limit_of_length):
		self.number_of_node = number_of_node
		self.upper_limit_of_length = upper_limit_of_length
		self.alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		self.letters = self.generate_letters_list()
		self.linked_list = []
		self.vertices = []
		self.generate_random_linked_list()
		self.generate_random_digraph()

	def generate_letters_list(self):
		letters = []
		while len(letters) != self.number_of_node:
			letter = self.alphabets[rd(0,25)]
			if letter not in letters:
				letters.append(letter)
		return letters

	def generate_random_linked_list(self):
		first_letter = self.letters[rd(0, len(self.letters)-1)]
		self.letters.remove(first_letter)
		first = node(first_letter, 0, 1)
		self.linked_list.append(first)
		self.generate_other_elements(first)

	def generate_other_elements(self, previous):
		if len(self.letters)>0:
			current_letter = self.letters[rd(0, len(self.letters)-1)]
			self.letters.remove(current_letter)
			if len(self.letters) == 0:
				hasNext = 0
			else:
				hasNext = 1
			current_node = node(current_letter, 1, hasNext)
			current_node.set_previous(previous)
			previous.set_next(current_node)
			self.linked_list.append(current_node)
			self.generate_other_elements(current_node)
		else:
			return False

	def generate_random_digraph(self):
		for node in self.linked_list:
			add_vertice = vertice(node.name)
			self.vertices.append(add_vertice)
		for node_1 in self.linked_list:
			vertice_1 = self.node_to_vertice(node_1)
			if node_1.hasNext == 1:
				length = rd(1,self.upper_limit_of_length)
				vertice_1.add_linked_vertices(self.node_to_vertice(node_1.next), length)
			for node_2 in self.linked_list:
				connected = rd(0,1)
				if node_2.name != node_1.name and vertice_1.has_linked_vertice(node_2.name):
					if connected == 1:
						length = rd(1,self.upper_limit_of_length)
						vertice_1.add_linked_vertices(self.node_to_vertice(node_2), length)

	def node_to_vertice(self, node):
		for vertice in self.vertices:
			if node.name == vertice.name:
				return vertice
		return None

	def get_vertices(self):
		return self.vertices



