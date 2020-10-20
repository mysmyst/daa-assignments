
def shortestDist(graph): 
	global X 

	# dist[i] is going to store shortest 
	# distance from node i to node N-1. 
	dist = [0] * N 

	dist[N - 1] = 0

	# Calculating shortest path 
	# for rest of the nodes 
	for i in range(N - 2, -1, -1): 

		# Initialize distance from 
		# i to destination (N-1) 
		dist[i] = X 

		# CheSck all nodes of next stages 
		# to find shortest distance from 
		# i to N-1. 
		for j in range(N): 
			
			# Reject if no edge exists 
			if graph[i][j] == X: 
				continue

			# We apply recursive equation to 
			# distance to target through j. 
			# and compare with minimum 
			# distance so far. 
			dist[i] = min(dist[i], 
						graph[i][j] + dist[j]) 

	return dist[0] 

# Driver code 
N = 8
X = 999999999999

graph =[[X, 1, 2, 5, X, X, X, X], 
		[X, X, X, X, 4, 11, X, X], 
		[X, X, X, X, 9, 5, 16, X], 
		[X, X, X, X, X, X, 2, X], 
		[X, X, X, X, X, X, X, 18], 
		[X, X, X, X, X, X, X, 13], 
		[X, X, X, X, X, X, X, 2]] 

node=input("enter number of nodes in graph\n")
for i in range(node):
    print("enter "+i+)
for conn in node:
    for node in graph:
        pass


print(shortestDist(graph)) 

# who is this
