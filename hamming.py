#restricted to those strings who have the same length
def hammingDistance(X,Y):
    i=0
    count=0
    for i in range(len(X)):
        if X[i] != Y[i]:
            count += 1
    return count 


X = "geekspractice"
Y = "nerdspractise"
res = hammingDistance(X,Y)
print(res)