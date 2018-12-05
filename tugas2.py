import numpy as nu 
import csv

# import untuk membaca file excel dan write data 

data = nu.genfromtxt("DataTugas2.csv", delimiter=",")
data = data[1:,1:]



pr= 0
pm= 0
pt= 0
ur= 0
ut= 0
j=0
k =1 
temp=[]

for x in range (len(data)) :
	pendapatan = data[x][0]
	hutang = data[x][1]
	terima = 0
	tolak = 0

	# pendatan rendah
	if (pendapatan < 0.5 ):
		pr=1
	elif(pendapatan >= 0.5 ) and (pendapatan <= 1):
		pr=( pendapatan-0.5) / (1-0.5)
	else:
		pr = 0
	# pendapatan sedang 
	if(pendapatan < 0.5) :
		pm = 0
	elif(pendapatan >= 0.5) and (pendapatan <= 1) :
		pm = (pendapatan - 0.5) / (1-0.5)
	elif (pendapatan > 1) and (pendapatan < 1.5) :
		pm = 1
	elif (pendapatan >= 1.5) and (pendapatan <= 2 ) :
		pm = (pendapatan-1.5)/(2- 1.5)
	else :
		pm = 0
	# pendapatan tinggi 
	if (pendapatan < 1.5) :
		pt = 0
	elif (pendapatan >= 1.5) and (pendapatan <= 2) :
		pt = (pendapatan - 1.5)/(2-1.5)
	else :
		pt = 1
	# hutang rendah 
	if (hutang < 25) :
		ur = 1
	elif (hutang >= 25) and (hutang <= 50) :
		hr = (hutang - 25)/(50-25)
	else :
		hr = 0

	# hutang tinggi 
	if (hutang < 25):
		ht = 0
	elif (hutang >= 25) and (hutang <=50) :
		ht =(hutang - 25) / (50-25)
	else:
		ht =1
	# aturan untuk diterima atau ditolaknya 
	if (pr >0 and hr > 0) :
		terima = max(terima,min(pr,hr))
	elif (pr >0 and ht >0 ) :
		terima = max(terima,min(pr,ht))
	elif (pm >0 and hr >0) :
		tolak = max(tolak,min(pm,hr))
	elif (pm > 0 and ht >0) :
		tolak= max(tolak,min(pm,ht))
	elif (pt >0 and hr>0) :
		tolak= max(tolak,min(pt,hr))
	elif (pt >0 and ht >0):
		tolak=max(tolak,min(pt,ht)) 

	# defuzzifikasi
	if terima == 0 and tolak == 0 :
		sugeno = 0
	else:
		sugeno = ((terima*80) + (tolak*39))/(tolak+terima)
	print("no :",x,"nilai :",sugeno)

	# Banyak data yang diterima
	if sugeno > 39 :
		j = j+1
	
	if k <= 20 and sugeno >39 :
	
		k= k+1
		temp.append(x+1)
		
# memasukan data ke TebakanTugas2.csv
a= nu.asarray(temp)
nu.savetxt("TebakanTugas2.csv",a,delimiter=",", fmt='%10.5f')


print("Diterima :" , j)

