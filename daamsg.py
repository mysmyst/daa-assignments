
node=input("enter number of nodes in graph\n")
node=int(node)
stages=input("enter number of stages of graph\n")
stages=int(stages)
graph=[]
x = 9999
dest=[0]*node
path=[0]*stages
path[0]=0
path[stages-1]=node-1

for i in range(node-1):
    inner=[]
    for j in range(node):
        inner.append(x)
    graph.append(inner)

for i in range(node-1):
    for j in range(i+1,node):
        print("enter distance of "+str(i)+"th node to "+str(j)+"th node. enter x if they are not connected")
        inp=input()
        if inp=='x':
            graph[i][j]=x
        else:
            graph[i][j]=int(inp)
  
dist = [0]*node 
dist[node-1]=0

for i in range(node-2,-1,-1): 
    dist[i]=x 
    for j in range(node):
        if graph[i][j]==x: 
            continue
        if dist[i]>=min(dist[i],graph[i][j]+dist[j]):
            dist[i]=min(dist[i],graph[i][j]+dist[j])
            dest[i]=j

print("shortest distance from first node to final node is:")         
print(dist[0])

print("path to sink is:")
for i in range(1,stages-1):
    path[i]=(dest[path[i-1]])
print(path)