import networkx as nx
import matplotlib.pyplot as plt

class edge:
	def __init__(self, u, v ,w):
		self.u=u
		self.v=v
		self.w=w
def sort(graph):
	for i in range(int(n)):
		for j in range(int(n)-1):
			if(graph[j].w>graph[j+1].w):
				tmp=graph[j]
				graph[j]=graph[j+1]
				graph[j+1]=tmp

def makeset(x):
	parent.append(x)
	rank.append(0)

def find(x):
	while (x != parent[x]):
		x=parent[x]
	return x



def union(x, y):
    parentU = find(x)
    parentV = find(y)
    if(parentU==parentV):
        return false
    if(rank[parentU]>rank[parentV]):
        parent[parentV]=parentU
    else:
        parent[parentU]=parentV
        if(rank[parentU]==rank[parentV]):
            rank[parentU]+=1


khung=[]
parent=[]
rank=[]

print("Nhap so dinh, canh:\n")
m=7
n=11
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
graph.append((edge(0, 1, 7)))
graph.append((edge(0, 3, 5)))
graph.append((edge(3, 1, 9)))
graph.append((edge(1, 2, 8)))
graph.append((edge(3, 4, 15)))
graph.append((edge(4, 1, 7)))
graph.append((edge(4, 2, 5)))
graph.append((edge(3, 5, 6)))
graph.append((edge(5, 4, 8)))
graph.append((edge(5, 6, 11)))
graph.append((edge(6, 4, 9)))

print("cac canh cua do thi:")
for x in range(int(n)):
	print(graph[x].w)
print("\n")

for x in range(int(m)):
	makeset(x)

sort(graph)
for x in range(int(n)):
	print(graph[x].w)

for x in range(int(n)):
	if (find(graph[x].u) != find(graph[x].v)):
		if(graph[x].u<graph[x].v): #đúng thứ tự thì mới hiển thị chuẩn
			khung.append((str(graph[x].u), str(graph[x].v)))
		else:
			khung.append((str(graph[x].v), str(graph[x].u)))
		union(graph[x].u, graph[x].v)
print(khung)

G=nx.DiGraph()
for x in range(int(n)):
	if(graph[x].u<graph[x].v):#đúng thứ tự
		G.add_edges_from([(str(graph[x].u), str(graph[x].v))], weight=graph[x].w)
	else:
		G.add_edges_from([(str(graph[x].v), str(graph[x].u))], weight=graph[x].w)

print(G.edges)

val_map = {'A': 1.0,
                   'D': 0.5714285714285714,
                              'H': 0.3}
values = [val_map.get(node, 0.75) for node in G.nodes()]

red_edges = khung 
edge_colors = ['blue' if not edge in red_edges else 'red' for edge in G.edges()]
edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])

pos=nx.spring_layout(G)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw(G, pos, node_color = values, node_size=150, edge_color=edge_colors, edge_cmap=plt.cm.Reds)
plt.show()                                            