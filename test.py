from digraph import digraph
from dijkstra_queue import dijkstra_queue
from dfs import dfs
from bfs import bfs
import numpy as np

# new_digraph = digraph(5,50)

# new_paths = dijkstra_queue(new_digraph)

# filename = 'dijkstra_queue.npy'
# vertices_paths = np.load(filename)

# for vertice in vertices_paths:
# 	print('Start Vertice: ' + vertice['start_vertice'].name)
# 	for path in vertice['shortest_paths']:
# 		print('End Vertice: ' + path['end_vertice'].name)
# 		print('Distance: ' + int(path['distance']))
# 		pa = ''
# 		for p in path['path']:
# 			pa+=p.name+' '
# 		print('Shortest Path: ' + pa)

new_list = digraph(4,50)

vertices = new_list.get_vertices()

for vertice in vertices:
	print('Vertice name: ' + vertice.name)
	for linked_vertice in vertice.linked_vertices:
		print('Linked Vertice Name: ' + linked_vertice['vertice'].name)
		print('Length: ' + str(linked_vertice['length']))
	print('\n')

start=raw_input("Start: ")

dfs = dfs(vertices,start)
bfs = bfs(vertices,start)
