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
			nx.draw_networkx_edge_labels(G,pos,edge_labels={(u, v): wt}, font_color  = 'red') #tambah label ke edge
		#plt.axis('off') bingung sbnernya buat apa
		plt.show(block = False) #display graf
	def keep(self):
		plt.show()
