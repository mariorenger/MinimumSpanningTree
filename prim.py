import networkx as nx
import matplotlib.pyplot as plt

class edge:
	def __init__(self, u, v ,w):
		self.u=u
		self.v=v
		self.w=w

def extract_min(min):	
	for x in range(int(m)):
		if(cost[x]<cost[min] and free[x]==True and trangthai[x]==False):
			min=x
	return min

print("Nhap so dinh, canh:\n")
m=6
n=10
# m=input()
# n=input()
graph =[]
# for x in range(int(n)):
# 	print("canh thu "+str(x))
# 	u=int(input(), base=10)
# 	v=int(input(), base=10)
# 	w=int(input(), base=10)
# 	edge(u, v, w)
# 	graph.append((edge(u, v, w)))
graph.append((edge(0, 1, 5)))
graph.append((edge(0, 2, 6)))
graph.append((edge(0, 3, 4)))
graph.append((edge(1, 3, 2)))
graph.append((edge(1, 2, 1)))
graph.append((edge(2, 3, 2)))
graph.append((edge(4, 2, 5)))
graph.append((edge(2, 5, 3)))
graph.append((edge(3, 5, 4)))
graph.append((edge(4, 5, 4)))


for x in range(int(n)):
	print(graph[x].w)
print("\n")

khung=[]
cost=[]
prev=[]
free=[]
trangthai=[]
for x in range(int(m)):
	cost.append(100000)
	prev.append(-1)
	free.append(False)
	trangthai.append(False)

min=4
cost[min]=0
free[min]=True
while (len(khung)<int(m)):
	print(cost)
	print(prev)
	print(khung)
	print('\n')
	min=extract_min(min)

	khung.append(min)
	for y in range(int(n)):
		if (graph[y].u==min and trangthai[graph[y].v]==False):
			if(cost[graph[y].v]>graph[y].w): 
				cost[graph[y].v]=graph[y].w
				prev[graph[y].v]=min				
			free[graph[y].v]=True

		if (graph[y].v==min and trangthai[graph[y].u]==False):
			if(cost[graph[y].u]>graph[y].w):
				cost[graph[y].u]=graph[y].w
				prev[graph[y].u]=min				
			free[graph[y].u]=True
	trangthai[min]=[True]
	cost[min]=100		
prev[khung[0]]=khung[1]			
			

print("\n")
print(khung)

G=nx.DiGraph()
for x in range(int(n)):
	if(graph[x].u<graph[x].v):#đúng thứ tự
		G.add_edges_from([(str(graph[x].u), str(graph[x].v))], weight=graph[x].w)
	else:
		G.add_edges_from([(str(graph[x].v), str(graph[x].u))], weight=graph[x].w)
val_map = {'A': 1.0,
           'D': 0.5714285714285714,
           'H': 0.0}
 
values = [val_map.get(node, 0.25) for node in G.nodes()]
print(prev)

red_edges=[]
for x in range(int(m)):
	if ((x)<prev[x]):
		red_edges.append((str(x), str(prev[x])))
	else:
		red_edges.append((str(prev[x]), str(x)))

edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]
edge_labels = dict([((u,v),d['weight'])
                 for u,v,d in G.edges(data=True)]) 

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(G, pos,)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()