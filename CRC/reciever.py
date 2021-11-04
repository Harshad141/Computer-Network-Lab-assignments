def xor(a, b):  #function for defining xor operation
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')   
    return ''.join(result)
 
def div(divident, divisor):  #modulo-2 divison
    K = len(divisor)
    temp = divident[0 : K]
    while K < len(divident):
        if temp[0] == '1':
            temp = xor(divisor, temp) + divident[K]
        else:   
            temp = xor('0'*K, temp) + divident[K]
        K += 1
    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0'*K, temp)
   
    dataword101 = temp
    return dataword101
def reciver():
    key="1011"                       #input key value
    dataword= "11010010"             #input the encoded-bit
    print("encoded data"+dataword)
    print("key/divisor:",key)
    K=len(key)
    decode_data=dataword + '0'*(K-1)
    rem1=div(dataword, key)   #calling the modulo-2 divison function
    #print(rem1)
    temp = "0" * (K - 1)
    if rem1 == temp:
        print("The message received is correct without any interference")
    else:
        print("The message received is incorrect")
reciver()   
