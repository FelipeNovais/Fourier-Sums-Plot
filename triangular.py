###################FOURIER FOR TRIANGULAR WAVE######################
#			-Created by Felipe Novais & Estela Mello-
#		-Dedicated to Renato Cantao great guy and teacher-
#
#		How to: call the triangular.py with summation n-index
#		example:
#				$python triangular.py 3
#				will result the first 3 terms
####################################################################

#IMPORTS
import sys
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, arange

#VARIABLES
x = arange(-3, 3, 0.0001)
y = (0.5)
#Step function f(x)
x2 = [-3,-2,-1,0,1,2,3]
y2 = [ 1, 0, 1,0,1,0,1]

#PROCESSING THE SUMMATION
if len(sys.argv) < 2:
	j = 2
else:
	j = int(sys.argv[1]) + 1
for i in range(1, j):
	if(i % 2):
		y += -1*(4/(i**2*pi**2))*cos(i*pi*x)
term = str(j-1)

#PLOTING
plt.plot(x, y,'b', label=r'$S_{'+term+'}(x)$', zorder=2) #Fourier series
plt.plot(x2, y2,'r', label=r'$f(x)$', zorder = 1) #Triangular wave
plt.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)

#SHOWING
plt.axes().set_ylim([-.5, 1.5])
plt.axes().set_aspect(1, 'box')
plt.grid()
plt.savefig('triangular'+term+'.png')  #comment this line if dont want to save plot to png image
plt.show()
