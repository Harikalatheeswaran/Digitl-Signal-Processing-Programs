import numpy as np

print('\nInput the values separated by commas.\n')

def row_insert():
   arr = []
   a = input('Enter the elements : ')
   t = a.split(',')
   for i in t:
      i = float(i)
      arr.append(i)
   return arr

print('\nEnter x(n) values: ')
x_n = np.array(row_insert())
print('\nEnter h(n) values: ')
h_n = np.array(row_insert())

a = np.zeros((len(x_n),len(x_n)))

for i in range(0, len(h_n)):
   for j in range(0, len(x_n)):
      a[i,j] = h_n[i]*x_n[j]

y_n = []
b = np.fliplr(a)

for i in range(-len(x_n),len(x_n)):
   x = b.diagonal(i)
   y_n.append(sum(x))

y_n.reverse()
l = len(y_n) - (len(x_n)+len(h_n) - 1)
print('\nThe output y(n) :\n',y_n[:-l])
