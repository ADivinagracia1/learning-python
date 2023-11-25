def findJudge(n, trust):
    trusted_by = [0] * (n+1)
    trusts_to = [0] * (n+1)

    for a, b in trust:
        print(a, b, trust)
        trusted_by[b] += 1
        trusts_to[a] += 1
    
    print()
    print(trusts_to)
    print("is trusted by")
    print(trusted_by)
    

n = 3
trust = [[1,3],[2,3]]

n = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

findJudge(n, trust)