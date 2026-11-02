import timeit

def Combinations(i, X, Y = []):
    A = X.copy()
    ret = Y.copy()

    if(len(ret) >= i):
        print(ret)
        return
    
    if(A == []):
        return


    Z = ret.copy()
    Z.append(A[0])
    Combinations(i, A[1:], Z)
    Combinations(i, A[1:], ret)
    
if __name__ == '__main__':
    A = list(range(10))
    Combinations(len(A)//2, A)
    #print(timeit.timeit('Combinations(len(A)//2, A)', number=10, globals=globals()))
