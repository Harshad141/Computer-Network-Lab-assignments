def main():
  ip,n = input("Enter the IP Address: ").split("/")
  no_of_sub_blocks = int(input("Enter the number of Sub blocks: "))
  sub_blocks = []
  for i in range(no_of_sub_blocks):
    sub_blocks.append(int(input("Enter the sub block: ")))
  print(Range(ip,int(n)))
  print(SubBlocks(sub_blocks,ip))
  print(Class(ip))
 
def BinaryToDecimal(binary):
  decimal = int(binary,2)
  return decimal
 
def DecimalToBinary(decimal):
  binary = (format(decimal,'08b'))
  return binary
 
def Class(ip):
  add = ip.split('.')
  a = int(add[0])
  if (a >= 0 and a <= 127):
	classs = "Belongs to Class A"
  elif (a >= 128 and a <= 191):
	classs = 'Belongs to Class B'
  elif (a >= 192 and a <= 223):
	classs = 'Belongs to Class C'
  elif (a >= 224 and a <= 239):
	classs = 'Blocngs to Class D'
  else:
	classs = 'Belongs to Class E'
  return classs
 
def nearpow2(subnet):
  v = 0
  p = 0
  array1 = []
  if subnet == 10:
	v = 16
	p = 4
  elif subnet == 60:
	v = 64
	p = 6
  elif subnet == 120:
	v = 128
	power = 7
  array1.append(v)
  array1.append(p)
  return array1
 
def Range(ip,n):
  add = ip.split('.')
  binary_address = ""
  req1 = ''
  req2 = ''
  for i in add:
    binary_address += DecimalToBinary(int(i))
  m = 32 - n
  req = binary_address[-m:]
  for i in req:
	if i == '1':
  	req1 += '0'
	else:
  	req1 += i
  low_req = binary_address[0:n] + str(req1)
  for i in req:
	if i == '0':
  	req2 += '1'
	else:
  	req2 += i
  up_req = binary_address[0:n] + str(req2)
  address = []
  low = ""
  up = ""
  for i in range(len(low_req)):
	if i%8 == 0:
  	r = BinaryToDecimal(low_req[i:i+8])
  	low += str(r) + "."
  for i in range(len(up_req)):
	if i%8 == 0:
  	r = BinaryToDecimal(up_req[i:i+8])
  	up += str(r) + "."
  address.append(low[:len(low)-1])
  address.append(up[:len(up)-1])
  return address 
 
def SubBlocks(sub_blocks,ip):
  add1 = ip.split('.')
  val = []
  multiple_address = []
  for i in range(len(sub_blocks)):
    val.append(nearpow2(sub_blocks[i]))
  for i in range(len(sub_blocks)):
	sum_ = 0
	for j in range(i+1):
  	sum_ += val[j][0]
	up = add1[0] + "." + add1[1] + "." + add1[2] + "." + str(sum_ - 1) + '/' + str(32 - val[i][1])
	low = add1[0] + "." + add1[1] + "." + add1[2] + "." + str(sum_ - val[i][0]) + '/' + str(32 - val[i][1])
    multiple_address.append([low,up,val[i][0]])
  return multiple_address
 
main()
