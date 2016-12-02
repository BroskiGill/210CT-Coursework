##Pseudocode
## graph<-{0: [1,5,2],
##         1: [0,2,4],
##         2: [1,0,3],
##         3: [2,],
##         4: [1,],
##         5: [0,],
##}
##  addNode(graph,node)
##     IF node NOT IN Graph
##         graph[node]<- emptyList

##  addEdge(graph,node1,node2)
##     IF node1 IN graph
##         graph[node1].push(node2)
##         graph[node2].push(node1)
##     ELSE:
##         graph[node1]<-[node2]
##         graph[node2].push(node1)
## addNode(graph,7)
## addEdge(graph,7,5)
## PRINT graph
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

addNode(graph,7)
addEdge(graph,7,5)

print(graph)
