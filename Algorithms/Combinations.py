import timeit

count = 0
count2 = 0

def Combinations(i, X, Y = []):
    global count
    global count2
    A = X.copy()
    ret = Y.copy()

    if(len(ret) >= i):
        print(ret)
        count += 1
        return
    
    if(A == []):
        count2 += 1
        return


    Z = ret.copy()
    Z.append(A[0])
    Combinations(i, A[1:], Z)
    Combinations(i, A[1:], ret)
    
if __name__ == '__main__':
    n = 10
    i = n//2
    A = list(range(n))
    Combinations(i, A)
    #print(f"n = {n}\ni = {i}\ncount == {count}\ncount2 == {count2}\ntotal == {count+count2}")
    #print(timeit.timeit('Combinations(len(A)//2, A)', number=10, globals=globals()))
