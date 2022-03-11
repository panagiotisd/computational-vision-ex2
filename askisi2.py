#PANAGIOTIS NTOUNETAS AM:2781

import numpy as numpy
from numpy import *
import matplotlib.pyplot as matplot
from PIL import Image
import sys


#Dhmiourghsa mia voithitikh synarthsh gia na mporo na eimai eyeliktos me ta orismata.
def aftrans(Taffine, a1, a2, a3, a4, a5, a6):

	m = input.shape[0] #grammes, mhkos
	n = input.shape[1] #sthles, ypsos
	
	Taffine = numpy.zeros([m,n])

	for i in range(0,m):
		for j in range(0,n):
			x1 = i - m//2
			y1 = j - n//2
			x2 = a1*x1 + a2*y1 + a3*1		#Ftiaxnw thn 1h seira tou T-affine pinaka
			y2 = a4*x1 + a5*y1 + a6*1		#2h seira
			
			if(a1 == -1):					#---
				x2 = -a1*x1 + -a2*y1 + a3*1	#Edw koitaw gia to rotate
				y2 = -a4*x1 + -a5*y1 + a6*1	#---
				
			m2 = x2 + m//2					#Ta dipla sumvola diaireshs einai gia na ginei amesws h diairesh me INT apotelesma
			n2 = y2 + n//2					
			strog_m2 = round(m2)			#Strogulopoiw me thn round dioti eixa error gia incomaptible types (logiko)
			strog_n2 = round(n2)		
			if((m2 >= 0 and m2 < m) and (n2 >= 0 and n2 < n)):	#Elegxw kai ftiaxnw thn eikona mou
				Taffine[i][j] = input[strog_m2][strog_n2]
	return Taffine

'''
#######################################################################
'''

#Eisagw thn eikona san orisma 



input = numpy.array(Image.open(sys.argv[1])) #inputs apo cmd/termatiko eikona, eikona pou vgainei, a1-a6
output = sys.argv[2]
a1 = float(sys.argv[3])
a2 = float(sys.argv[4])
a3 = float(sys.argv[5])
a4 = float(sys.argv[6])
a5 = float(sys.argv[7])
a6 = float(sys.argv[8])
'''
input = numpy.array(Image.open('brain_graphy.png'))			#Block entolwn gia na to treksw sto Jupyter apokleistika.
output = 'new_brain.png'
print(output, '<- Onoma pragomenou arxeiou gia ton Jupyter.')
print('Test gia Shear.')
a1 = 1
a2 = 0
a3 = 0
a4 = 0
a5 = 1
a6 = 0
'''
out = aftrans(input, a1, a2, a3, a4, a5, a6)

matplot.imshow(out, cmap = 'gray')
matplot.show()
Image.fromarray(out.astype(numpy.uint8)).save(output) #Se ayth thn askhsh kanw kai save thn einkona gia na to dokimasw an paizei sosta kai epeidh zhteitai kai output arxeio. 
