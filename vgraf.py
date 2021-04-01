import networkx as nx
import matplotlib.pyplot as plt
#ini masi coba2
class GraphVisualization:
	#listedge
	def __init__(self):
		self.listedge = []
		
	# addEdge
	def addEdge(self, a, b, c):
		temp = [a, b, c]
		self.listedge.append(temp)

	def visualize(self):
		G = nx.Graph() #graf dari networkx
		G.add_weighted_edges_from(self.listedge) #tambah sisi dari listedge
		pos = nx.spring_layout(G)
		nx.draw(G,pos,edge_color='black',width=1,linewidths=1, node_size=500,node_color='blue',alpha=0.9, labels={node:node for node in G.nodes()})
		for (u, v, wt) in G.edges.data('weight'):
			nx.draw_networkx_edge_labels(G,pos,edge_labels={(u, v): wt}, font_color  = 'red')
		#plt.axis('off') g tau buat apa
		plt.show(block = False) #display graf
	def keep(self):
		plt.show()

# Driver code
if __name__ == '__main__':
	'''G = GraphVisualization()
	G.addEdge(0, 2, 1.5)
	G.addEdge(1, 2, 1)
	G.addEdge(1, 3, 2)
	G.addEdge(5, 3, 5)
	G.addEdge(3, 4, 3.5)
	G.addEdge(1, 0, 6)
	G.visualize()
	G.keep()'''
	edges = [['A','B'],['B','C'],['B','D']]
	G = nx.Graph()
	G.add_edges_from(edges)
	pos = nx.spring_layout(G)
	plt.figure()    
	nx.draw(G,pos,edge_color='black',width=1,linewidths=1,\
	node_size=500,node_color='pink',alpha=0.9,\
	labels={node:node for node in G.nodes()})
	nx.draw_networkx_edge_labels(G,pos,edge_labels={('A','B'):'AB',\
	('B','C'):'BC'}, font_color='red')
	nx.draw_networkx_edge_labels(G,pos,edge_labels={('B', 'D'): 'BD'}, font_color  = 'blue')
	plt.axis('off')
	plt.show()
