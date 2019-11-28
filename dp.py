def dp(X,Y,m,n):
    if m==0:
        return n
    if n==0:
        return m
    if X[m-1]==Y[n-1]:
        return dp(X,Y,m-1,n-1)
    return 1 + min(dp(X,Y,m-1,n), dp(X,Y,m,n-1), dp(X,Y,m-1,n-1))

def dpEditDistance(X,Y):
    m = len(X)
    n = len(Y)
    ed = dp(X,Y,m,n)
    return ed

X = "food"
Y = "foooooooood"
res = dpEditDistance(X, Y)
print(res)