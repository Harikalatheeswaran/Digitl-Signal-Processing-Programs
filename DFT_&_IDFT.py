import math

p = math.pi
choice = input('1 for DFT....2 for IDFT :\n')

if choice == '1':
   # DFT
   print('Input the values separated by comma , !')
   a = input('Enter : ')
   b = a.split(',')
   x = []
   for i in b:
      i = complex(i)
      x.append(i)
   N = len(x)
   x_out = []
   x_temp = 0+0j

   for k in range(0,N):
      for n in range(0,N):
         c = math.cos((2*p*k*n)/N)
         s = math.sin((2*p*k*n)/N)
         c = round(c)
         s = round(s)
         m = complex(c,-s)
         
         x_temp = x_temp + (x[n]*m)
      x_out.append(x_temp)
      x_temp = 0
   print('\n   The Values :   \n')
   for i in x_out:
      print(i)

elif choice == '2s':
   # IDFT
   print('Input the values separated by comma , !')
   a = input('Enter : ')
   b = a.split(',')
   x = []
   for i in b:
      i = complex(i)
      x.append(i)
   N = len(x)
   x_out = []
   x_temp = 0+0j

   for k in range(0,N):
      for n in range(0,N):
         c = math.cos((2*p*k*n)/N)
         s = math.sin((2*p*k*n)/N)
         c = round(c)
         s = round(s)
         m = complex(c,s)
         
         x_temp = x_temp + (x[n]*m)
      x_out.append((x_temp)/N)
      x_temp = 0
   print('\n   The Values :   \n')
   for i in x_out:
      print(i)

else:
   print('DUDE ?!')




