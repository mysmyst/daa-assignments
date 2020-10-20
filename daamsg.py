
node=input("enter number of nodes in graph\n")
node=int(node)

graph=[]
x = 99999999

for i in range(node-1):
    inner=[]
    for j in range(node):
        inner.append(x)
    graph.append(inner)

for i in range(node-1):
    for j in range(i+1,node):
        print("enter distance of "+str(i+1)+"th node to "+str(j+1)+"th node. enter x if they are not connected")
        inp=input()
        if inp=='x':
            graph[i][j]=x
        else:
            graph[i][j]=int(inp)

def MSG(graph,node,x):  

	dist = [0]*node 
	dist[node-1]=0

	for i in range(node-2,-1,-1): 
		dist[i]=x 
		for j in range(node):
			if graph[i][j]==x: 
				continue
			dist[i]=min(dist[i],graph[i][j]+dist[j]) 
	return dist[0] 

print("shortest distance from first node to final node is:")         
print(MSG(graph,node,x)) 
