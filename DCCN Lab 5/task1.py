import numpy as np

def even_parity(seq):
    sum = None
    for d in seq: 
        if sum == None:
            sum = d
        else:
            sum = sum ^ d
    
    return False if sum else True
     
def rect_parity(codeword, nrows, ncols):
    
    data_bits_len = nrows*ncols
    shape = ( nrows, ncols )
    data_bits = codeword[:data_bits_len].reshape( shape )
    
    R = codeword[data_bits_len:data_bits_len+nrows].tolist()
    C = codeword[data_bits_len+nrows:data_bits_len+nrows+ncols].tolist()
    
    print('Databits: ')
    print(data_bits)
    
    row_sum = []
    for row in data_bits:
        if even_parity(row):
            row_sum.append(0)
        else:
            row_sum.append(1)
    
    col_sum = []
    for row in data_bits.transpose():
        if even_parity(row):
            col_sum.append(0)
        else:
            col_sum.append(1)

    print('Row Sum: ',row_sum)
    print('Column Sum: ',col_sum)
    
    print('Row parity bits: ',R)
    print('Column parity bits: ',C)
    
    r_error = 0
    c_error = 0
    row_flip = 0
    col_flip = 0
    for i in range(nrows):
        if row_sum[i] != R[i]:
            print("Parity error in row {}".format(i+1))
            r_error += 1
            row_flip = i
    
    for i in range(ncols):
        if col_sum[i] != C[i]:
            print("Parity error in column {}".format(i+1))
            c_error += 1
            col_flip = i
    
    message_sequence = data_bits
    if r_error == c_error:
        # print(row_flip,col_flip)
        if r_error == 1:
            message_sequence[row_flip,col_flip] = not(data_bits[row_flip,col_flip])
        elif r_error == 0:
            print('no correction is necessary')
        else:
            print('uncorrectable error is detected')
    else:
        print('uncorrectable error is detected')
        
    return message_sequence

def test_correct_errors():        
    nrows = 2
    ncols = 4
    codeword1 = np.array( [0, 1, 1, 0, 1, 1, 0, 1,
                        0,1, 
                        1, 0, 1, 1] )
    codeword2 = np.array( [1, 0, 0, 1, 0, 0, 1, 0,
                        1,1, 
                        1, 0, 1, 0] )  
    codeword3 = np.array( [0, 1, 1, 1, 1, 1, 1, 0,
                        1,1, 
                        1, 0, 0, 0] )  
    print('Codeword 1')
    rect_parity(codeword1,nrows,ncols)
    # if np.array_equal(result1,codeword1[:nrows*ncols].reshape(nrows,ncols)):
    #     print('Testing all 2**n = 256 valid codewords\n...passed')
    #     print('Testing all possible single-bit errors\n..passed')
    #     print('(8,4) rectangular parity code successfully passed all 0,1 and 2 bit error tests')
    print('\nCodeword 2')
    rect_parity(codeword2,nrows,ncols)
    print('\nCodeword 3')
    rect_parity(codeword3,nrows,ncols)


if __name__ == "__main__":
    test_correct_errors()
    


        
        
    
