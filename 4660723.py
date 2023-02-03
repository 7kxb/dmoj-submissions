n,m,a,b = map(int, input().split())
vertexList = []
edgeList = []
for i in range(1, n+1):
    vertexList.append(i)
for i in range(m):
    x,y = map(int, input().split())
    edgeList.append((x-1,y-1))
def dfs(vertexList, edgeList):
    adjacencyList = [[] for vertex in vertexList]
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])
    stack = [0]
    visitedVertex = []
    while stack:
        current = stack.pop()
        for neighbour in adjacencyList[current]:
            if not neighbour in visitedVertex:
                stack.append(neighbour)
        visitedVertex.append(current)
    for i in range(len(visitedVertex)):
        visitedVertex[i] += 1
    return visitedVertex
if a and b in dfs(vertexList, edgeList):
    print('GO SHAHIR!')
else:
    print('NO SHAHIR!')
# 
# 6 7 1 6
# 1 2
# 2 3
# 2 5
# 5 1
# 3 4
# 4 5
# 4 6
# 
# 6 6 1 6
# 1 2
# 2 3
# 2 5
# 5 1
# 3 4
# 4 5
#