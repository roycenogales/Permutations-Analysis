import random
import timeit

def MinChange(X, Y = [], flag = 'R'):
    A = X.copy() #creates a copy so that its not pass by reference
    ret = Y.copy() #creates a copy of the list so that its not pass by reference
    if(flag == 'R'):
        if(A == []):
            #print(ret)
            return
        
        ret.append(A.pop(0))
        if(len(ret) > 1):
            for i in range(len(ret)-1):
                if(i%2 == 0):
                    MinChange(A, ret, "R")
                else:
                    MinChange(A, ret, "L")
                x = ret[len(ret)-i-1]
                ret[len(ret)-i-1] = ret[len(ret)-i-2]
                ret[len(ret)-i-2] = x
                
            if(len(ret)%2 == 0):
                MinChange(A, ret, "L")
            else:
                MinChange(A, ret, "R")
        else:
            MinChange(A, ret, "R")
        
    else:
        if(A == []):
            #print(ret)
            return

        ret.insert(0, A.pop(0)) #inserts to the front of the list
        if(len(ret) > 1): ##this might be unnecessary as we can only insert left after inserting right initially
            for i in range(len(ret)-1):
                if(i%2 == 0):
                    MinChange(A, ret, "R")
                else:
                    MinChange(A, ret, "L")
                x = ret[i]
                ret[i] = ret[i+1]
                ret[i+1] = x
            if(len(ret)%2 == 0):
                MinChange(A, ret, "L")
            else:
                MinChange(A, ret, "R")
        else:
            MinChange(A, ret, "R")


if __name__ == '__main__':

    for i in range(1, 11, 1):
        n = i
        A = list(range(n))
    
        print(f"n = {n}| time:", timeit.timeit('MinChange(A)', number=10, globals=globals()))
