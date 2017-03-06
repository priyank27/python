#print('this si')

'''
x = 5
y = 10
if x < y:
	print('x is greater than y')
'''
'''

text = 'Sample Text to Save\nNew line!'

saveFile = open('exampleFile.txt','w')

saveFile.write(text)

saveFile.close()
'''
'''

appendMe = '\nNew bit of information'

appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()
'''


'''
readMe = open('exampleFile.txt','r').read()
print(readMe)
'''
'''

readMe = open('exampleFile.txt','r').readlines()
print(readMe)
'''
'''

x = raw_input('What is your name?: ')
print('Hello',x)

'''
'''

  (examplemod.py)  def ex(data):
    print(data)


import examplemod
examplemod.ex('test')

'''
'''

import statistics

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]

x = statistics.mean(example_list)
print(x)

y = statistics.median(example_list)
print(y)

z = statistics.mode(example_list)
print(z)

a = statistics.stdev(example_list)
print(a)

b = statistics.variance(example_list)
print(b)
'''



import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = input('What website to scan?: ')


def pscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False


for x in range(25):
    if pscan(x):
        print('Port',x,'is open')	



