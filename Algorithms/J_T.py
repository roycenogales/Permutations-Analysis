import timeit

def J_T(A, D):
    #count = 1 #previously used to track if all permutations were created
    #print(A) #, count)
    check = True
    while check == True:
        k = -1
        for i in range(len(A)):
            if(D[i] == "L" and i > 0 and A[i] > A[i-1]):
                if(k < 0): k = i
                elif(A[i] >= A[k]): k = i
            elif(D[i] == "R" and i < len(A)-1 and A[i] > A[i+1]):
                if(k < 0): k = i
                elif(A[i] >= A[k]): k = i
                    
        if(k == -1): return
        
        x = A[k]
        if(D[k] == "L"): swap(A, D, k, k-1)
        else: swap(A, D, k, k+1) 
        reverse(A, D, x)
        #count += 1
        #print(A) #, count)
        
def directionList(A):
    X = []
    for i in range(len(A)):
        X.append("L")
    return X

def swap(A, D, i, j):
    X = A[i], D[i]
    A[i], D[i] = A[j], D[j]
    A[j], D[j] = X

def reverse(A, D, x):
    for i in range(len(A)):
        if(A[i] > x and D[i] == "L"): D[i] = "R"
        elif(A[i] > x and D[i] == "R"): D[i] = "L"

if __name__ == '__main__':
    
    for i in range(1, 11, 1):
        n = i
        A = list(range(n))
        dirArr = directionList(A)
        print(f"n = {n}| time:", timeit.timeit('J_T(A, dirArr)', number=10, globals=globals()))
