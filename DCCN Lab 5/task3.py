import numpy as np
from syndrome_decode import syndrome_decode

G = np.array([[1,0,0,0,1,1,0],
			  [0,1,0,0,1,0,1],
			  [0,0,1,0,0,1,1],
			  [0,0,0,1,1,1,1]])

validcodewords = [np.array([i,j,k,l]) 
	for i in range(2) 
	for j in range(2) 
	for k in range(2) 
	for l in range(2)]

for i,codeword in enumerate(validcodewords):
	x1,x2,x3,x4 = codeword
	validcodewords[i] = np.append(codeword,[x1^x2^x4 , x1^x3^x4 , x2^x3^x4])

print("Testing all 2**k = 16 valid codewords")

for codeword in validcodewords:
	r = syndrome_decode(codeword,7,4,G)
	print("Tested codeword",codeword,"expected",codeword[:4],"got",r,"\n")
	if not np.array_equal(codeword[:4],r):
		print("OOPS: Error decoding",codeword,"...expected",codeword[:4],"got",r)
		quit()

print("...passed")

print("Testing all n*2**k = 112 single-bit error codewords")

for codeword in validcodewords:
	testcodeword = codeword.copy()
	for i in range(len(testcodeword)):
		testcodeword[i] ^= 1
		r = syndrome_decode(testcodeword,7,4,G)
		print("Tested codeword",testcodeword,"expected",codeword[:4],"got",r,"\n")
		if not np.array_equal(codeword[:4] , r):
			print("OOPS: Error decoding",testcodeword,"...expected",codeword[:4],"got",r)
		testcodeword[i] ^= 1

print("...passed")
print("All 0 and 1 error tests passed for (7,4,3) code with generator matrix G =")
print(G)
