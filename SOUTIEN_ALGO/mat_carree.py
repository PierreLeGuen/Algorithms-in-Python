def mat_dist(mat):
    n=len(mat)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if mat[i][j]<=mat[i][k]+mat[k][j]:
                    pass
                else:
                    return False
    return True

mat=[
    [0,5,8],
    [5,0,13],
    [8,3,0]
]
print(mat_dist(mat))