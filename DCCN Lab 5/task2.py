import numpy as np


def mod2(A):
    return np.mod(A,2)
    

def equal(a, b):
    return np.array_equal(a,b)


def syndrome_decode(codeword, n, k, G):
    
    #calculate A
    A = G[0:k,k:n]
    
    #calculate H
    At = A.transpose()
    I = np.identity(n-k,dtype=int)
    H = np.concatenate((At,I), axis=1)
    
    #calculate cdash
    rT = r.transpose()
    x = H.dot(rT)
    cdash = mod2(x)


    for i in range(k):
        #generate syndromes of interest
        T = np.array([0,0,0,0,0,0,0])
        T[i] = 1
        syndrome = H.dot(T.transpose())
        
        #check if syndrome is equal to
        if equal(syndrome,cdash):
            r[i] = not(r[i])
            break
    return(r[:k])

if __name__ == "__main__":
    n=7
    k=4
    G = np.array([1,0,0,0,1,1,0,
                0,1,0,0,1,0,1,
                0,0,1,0,0,1,1,
                0,0,0,1,1,1,1
                ]).reshape(k,n)

    c = np.array([1,0,1,0,1,0,1])   #correct code      
    r = np.array([1,1,1,0,1,0,1])   #error at position 2
    codeword =  r       
    message = syndrome_decode(codeword, n, k, G)  
    print(''.join(map(str,message.tolist())))
    





