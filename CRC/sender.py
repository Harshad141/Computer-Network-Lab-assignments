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
 
def sender(): 
    data="11010"                #input original data  
    key= "1011"                 #input key value
    print("original data:"+data)
    print("key/divisor:"+key)
    K=len(key)
    encode_data=data + '0'*(K-1) #calling the modulo-2 divison function
    rem=div(encode_data, key)
    dataword = data + rem
    print("encoded data:"+dataword) #encoded bits
    print("CRC bits:"+rem)  #CRC bits
sender() 
