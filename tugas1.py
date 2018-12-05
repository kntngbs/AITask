import random
import math

T=50000
c = 0.6
x1 = random.uniform(-10,10)
x2 = random.uniform(-10,10)
p1= math.sin(x1) * math.cos(x2)
e1= math.exp(math.fabs(1-(math.sqrt(pow(x1,2) + pow(x2,2)))/math.pi)) 

f1 = -1 * math.fabs(p1*e1)  
while (T > 0.00001):
	for i in range(0,100):
		y1 = random.uniform(-10,10)
		y2 = random.uniform(-10,10)
		p2= math.sin(y1) * math.cos(y2)
		e2= math.exp(math.fabs(1-(math.sqrt(pow(y1,2) + pow(y2,2)))/math.pi)) 
		f2 = -1 * math.fabs(p2*e2) 
		delta = f2 - f1
		 
		if (delta > 0 ):
			met = math.exp((-1 * delta)/T)
			r = random.random()
			if (r <= met):
				f1=f2
				
		else:
			f1=f2
		
		print("nilai minimum : ", f1, "iterasi ke - ", i)
	T = T*c
print("nilai minimum global = ", f1,"Dengan nilai x1 = ", x1 ,"dan x2 = ",x2)




	