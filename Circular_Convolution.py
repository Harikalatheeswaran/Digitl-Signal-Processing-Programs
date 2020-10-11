import numpy as np
print('\nNote:\nPlease Make sure that size of x(n) is > h(n) ')
print('Input the values separated by commas.\n')

def rotate(a):
   a.insert(0,a.pop())
   return a

def row_insert():
   arr = []
   a = input('Enter the elements : ')
   t = a.split(',')
   for i in t:
      i = float(i)
      arr.append(i)
   return arr

print('\nEnter x(n) values: ')
x_n = row_insert()
print('\nEnter h(n) values: ')
h_n = row_insert()

if not (len(x_n)==len(h_n) and (len(x_n)>len(h_n))):

   e = len(x_n)-len(h_n)

   for i in range(e):
      h_n.append(0)
 
   a = np.zeros((len(x_n),len(h_n)))
   b = np.zeros((len(h_n),1))
   b1 = x_n[0:1]
   b2 = x_n[1:]
   b2.reverse()
   arr = b1 + b2
   temp = arr
   a[0,] = temp

   for i in range(1,a.shape[0]):
      a[i,] = rotate(temp)
            
   for i in range(0,len(h_n)):
      b[i,] = h_n[i]

   c = np.dot(a,b)
   print('\nThe circular convolution of x(n) & h(n) is :')
   #print(c,'\n')
   c = c.reshape(len(h_n))
   print('y(n) is :\n',c)  
   
   
 