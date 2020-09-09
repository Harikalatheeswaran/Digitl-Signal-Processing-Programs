import cmath

pi = cmath.pi
choice = input('1 for DFT....2 for IDFT :\n')

if choice == '1':
   # DFT
   N = int(input('Enter the no.of samples i.e N = '))
   x = []
   count = 0
   
   for i in range(N):
      a = float(input('x({}) = '.format(count)))
      x.append(a)
      count += 1
   x_out = []
   x_temp = 0+0j

   for k in range(0,N):
      for n in range(0,N):
         e = cmath.exp(((-2*pi*n*k)/N)*1j)
         if N%2 == 0:
            m = complex(round(e.real,1),round(e.imag,1))
         else:
            m = complex(round(e.real,6),round(e.imag,6))
         
         x_temp = x_temp + (x[n]*m)
      x_out.append(x_temp)
      x_temp = 0
   print('\n   The Values :   \n')
   cc = 0
   for i in x_out:
      i = complex(round(i.real,6),round(i.imag,6))
      print('X({}) = {}'.format(cc,i))
      cc += 1 

elif choice == '2':
   # IDFT
   N = int(input('Enter the no.of samples i.e N = '))
   x = []
   count = 0
   for i in range(N):
      a = complex(input('X({}) = '.format(count)))
      x.append(a)
      count += 1
   x_out = []
   x_temp = 0+0j

   for k in range(0,N):
      for n in range(0,N):
         e = cmath.exp(((2*pi*n*k)/N)*1j)
         if N%2 == 0:
            m = complex(round(e.real,1),round(e.imag,1))
         else:
            m = complex(round(e.real,6),round(e.imag,6))

         x_temp = x_temp + (x[n]*m)
      x_out.append((x_temp)/N)
      x_temp = 0
      
   print('\n   The Values :   \n')
   cc = 0
   for i in x_out:
      a = int(round(i.real,1))
      print('x({}) = {}'.format(cc,a))
      cc += 1 
else:
   print('DUDE ?!')
   
