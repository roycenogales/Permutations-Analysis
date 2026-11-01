import random
import timeit

def MinChange(X, Y = [], flag = 'R'):
    A = X.copy() #creates a copy so that its not pass by reference
    ret = Y.copy() #creates a copy of the list so that its not pass by reference
    if(flag == 'R'):
        if(A == []):
            return
        
        ret.append(A.pop(0))
        print(ret)
        if(len(ret) > 1):
            for i in range(len(ret)-1):
                if(i%2 == 0):
                    MinChange(A, ret, "R")
                else:
                    MinChange(A, ret, "L")
                x = ret[len(ret)-i-1]
                ret[len(ret)-i-1] = ret[len(ret)-i-2]
                ret[len(ret)-i-2] = x
                print(ret)
                
            if(len(ret)%2 == 0):
                MinChange(A, ret, "L")
            else:
                MinChange(A, ret, "R")
        else:
            MinChange(A, ret, "R")
        
    else:
        if(A == []):
            return

        ret.insert(0, A.pop(0)) #inserts to the front of the list
        print(ret)
        if(len(ret) > 1): ##this might be unnecessary as we can only insert left after inserting right initially
            for i in range(len(ret)-1):
                if(i%2 == 0):
                    MinChange(A, ret, "R")
                else:
                    MinChange(A, ret, "L")
                x = ret[i]
                ret[i] = ret[i+1]
                ret[i+1] = x
                print(ret)
            if(len(ret)%2 == 0):
                MinChange(A, ret, "L")
            else:
                MinChange(A, ret, "R")
        else:
            MinChange(A, ret, "R")


if __name__ == '__main__':
    A = [1, 2, 3]
    MinChange(A)
    #print(f"this is A after function: {A}")
