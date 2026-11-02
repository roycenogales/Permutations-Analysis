import time
import timeit

def LexOrder(A):
    #check = True
    found = True
    while found == True:
        found = False
        x = -1
        y = -1
        print(A)
        for i in range(len(A)-1,0,-1):
            if(A[i-1] < A[i] and found == False):
                x = i-1
                found = True
        if(found == False): break
        for i in range(len(A)-1, x, -1):
            if(A[i] > A[x] and i > y): y = i
        swap(A, x, y)
        reverse(A, x+1)

def swap(A, i, j):
    X = A[i]
    A[i] = A[j]
    A[j] = X

def reverse(A, i):
    for j in range(i, len(A)-(len(A)-i)//2, 1):
        swap(A, j, len(A)-1-j+i)
        
if __name__ == '__main__':
    A = [1, 2, 3, 4]
    LexOrder(A)
