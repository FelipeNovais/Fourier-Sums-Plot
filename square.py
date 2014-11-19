###############FOURIER PARTIAL SUMS FOR SQUARE WAVE#################
#			-Created by Felipe Novais & Estela Mello-
#		-Dedicated to Renato Cantao great guy and teacher-
#
#		How to: call the square.py with summation n-index
#		example:
#				$python square.py 5
#				will result the first 5 terms
####################################################################

#IMPORTS
import sys
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, arange

#VARIABLES
#Fourier partial sums
x = arange(-2 * pi, 2 * pi, 0.0001)
y = (0.5)
#Step function f(x)
y2 = [1, 0, 1, 0, 1]
x2 = [-2 * pi, -pi, 0, pi, 2 * pi]
y3 = [0, 1, 0, 1, 0]

#DEFINING THE PLOT AREA
fig = plt.figure()
ax  = fig.add_subplot(111)
#Changing X axis labels to radians
x_label = [r"$-{2\pi}$", r"$-\pi$", r"$0$", r"$\pi$",   r"${2\pi}$"]
ax.set_xticks([-2*pi, -pi, 0, pi, 2*pi])
ax.set_xticklabels(x_label, fontsize=20)

#PROCESSING THE SUMMATION
if len(sys.argv) < 2:
	j = 2
else:
	j = int(sys.argv[1]) + 1
for i in range(1, j):
	if(i % 2):
		y += (2/(pi*i))*sin(i*x)

term = str(j-1)

#PLOTING
ax.plot(x, y, label=r'$S_{'+term+'}(x)$', zorder=999) #Fourier series
ax.step([-2 * pi, -pi],[1, 1],'r', [-pi, 0],[0, 0],'r', [0, pi],[1, 1],'r', [pi, 2 * pi],[0, 0], 'r') #f(x) "square wave"
ax.step(0,0,'r',label=r'$f(x)$') #f(X)	label
ax.scatter(x2, y2, s = 30, c = 'r', edgecolors ='r') #f(x) left boundaries
ax.scatter(x2, y3, s = 30, c = 'w', edgecolors ='r') #f(x) right boundaries
ax.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)

#SHOWING
plt.axes().set_ylim([-0.4, 1.4])
plt.axes().set_aspect(pi, 'box')
plt.grid()
plt.savefig('square'+term+'.png')  #comment this line if dont want to save plot to png image
plt.show()
