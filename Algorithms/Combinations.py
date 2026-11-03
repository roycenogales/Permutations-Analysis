import timeit

def Combinations(i, X, Y = []):
    A = X.copy()
    ret = Y.copy()

    if(len(ret) >= i):
        #print(ret)
        return
    
    if(A == []):
        return


    Z = ret.copy()
    Z.append(A[0])
    Combinations(i, A[1:], Z)
    Combinations(i, A[1:], ret)
    
if __name__ == '__main__':
    for i in range(1, 21, 1):
        n = i
        A = list(range(n))

        print(f"n = {n}| time:", timeit.timeit('Combinations(n//2, A)', number=10, globals=globals()))
