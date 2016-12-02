graph = {0: [1,5,2],
         1: [0,2,4],
         2: [1,0,3],
         3: [2,],
         4: [1,],
         5: [0,],
}
def addNode(graph, node):
    
    if node not in graph:

        #graph is equal to empty list if the node is not already in it 
        
        graph[node] = []

def addEdge(graph,node1,node2):
    if node1 in graph:

        #Adding node to edges
        
        graph[node1].append(node2)
        graph[node2].append(node1)
    else:
        
        graph[node1] = [node2]

        #This will add graph node2 to node1
        
        graph[node2].append(node1)

def dfs(graph, root):
#visited
    v = []
#stack
    s= [root, ]

    while s:
      #deleting the nodes
        node = s.pop()

        if node not in v:
          #adding nodes that have been visited
            v.append(node)

            s.extend([x for x in graph[node] if x not in v])
    return v

def bfs(graph, root):
#visited
    v = []
#queue
    q = [root, ]

    while q:
        # Deleting node in queue
        node = q.pop(0)

        if node not in v:
         # it will add nodes to the ones that have been visited
            v.append(node)
            
            
    
            q.extend([x for x in graph[node] if x not in v])

    return v



addNode(graph,7)
addEdge(graph,7,5)

print(dfs(graph,0))
print(bfs(graph,0))
