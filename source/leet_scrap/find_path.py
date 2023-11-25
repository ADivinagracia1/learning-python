def validPath(n, edges, source, destination):
    
    visited = set()
    stack = [source]
    adjacent = [[] for _ in range(n+1)]

    for a, b in edges:
        adjacent[a].append(b)
        adjacent[b].append(a)

    while len(stack)>0:
        v = stack.pop()
        visited.add(v)
        print(v)

        # # THIS CODE IS FOR DIRECTED GRAPHS
        # for src,des in edges:
        #     if v == src and des not in visited:
        #         stack.append(des)
        # # adj = [des for src,des in edges if v == src and des not in visited]
        
        # # LOOPS THROUGH ALL EDGES (must loop through Neighbors only)
        # for a,b in edges:
        #     print(a,b)
        #     if v == a and b not in visited:
        #         print("I am here! A")
        #         stack.append(b)
        #     if v == b and a not in visited:
        #         print("I am here! B")
        #         stack.append(a)

        for neighbor in adjacent[v]:
            if neighbor not in visited:
                stack.append(neighbor)

        print(stack)

        if v == destination:
            return True

    return False


n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

# n = 6
# edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
# source = 0
# destination = 5

# n = 10
# edges = [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
# source = 7
# destination = 5


print(validPath(n, edges, source, destination))
