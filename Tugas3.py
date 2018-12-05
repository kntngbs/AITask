import numpy as num 
import csv
import math as m
# import library

Dtrain = num.genfromtxt("DataTrain_Tugas3_AI.csv", delimiter=",")
Duji= num.genfromtxt("DataTest_Tugas3_AI.csv", delimiter=",")
Dtrain = Dtrain[1:,1:]
Duji = Duji[1:,1:]
# set data test dan uji
terbaik=0
q=0
tebak=[]

# perulangan untuk mencari K paling bagus sebanyak 200 kali
for x in range(199):
	hasil=[]
	betul=0
	n0=0
	n1=0
	n2=0
	n3=0
	x1=Dtrain[x][0]
	x2=Dtrain[x][1]
	x3=Dtrain[x][2]
	x4=Dtrain[x][3]
	x5=Dtrain[x][4]
	# perbandingan untuk membadingkan data uji yang akan mencari K terbaik
	for j in range(200,800):
		y1=Dtrain[j][0]
		y2=Dtrain[j][1]
		y3=Dtrain[j][2]
		y4=Dtrain[j][3]
		y5=Dtrain[j][4]
		h= m.sqrt(pow(x1-y1,2) + pow (x2-y2,2) + pow( x3-y3,2) + pow(x4-y4,2) + pow(x5-y5,2))
		row_list=[]
		row_list.append(j)
		row_list.append(h)
		hasil.append(row_list)
	# sorting untuk mengurutkan jarak data yang paling kecil 
	hasil.sort(key=lambda p: p[1])
	k=1
	# perulangan sebanyak 17 kali untuk menentukan yang terbaik 
	while (k <=17):
		# perulangan untuk menghitung tentangga 
		for z in range(k-1):
			if(Dtrain[hasil[z][0]][5] == 0):
				n0=n0+1
			elif(Dtrain[hasil[z][0]][5] == 1):
				n1=n1+1
			elif(Dtrain[hasil[z][0]][5] == 2):
				n2=n2+1
			else:
				n3=n3+1
		# kondisi untuk mengecek termasuk kelas yang mana 
		if(n1>n2 and n1>n3 and n1>n0):
			T=1
		elif(n0>n1 and n0>n2 and n0>n3):
			T=0
		elif(n2>n1 and n2>n0 and n2 >n3):
			T=2
		else:
			T=3

		# menghitung tebakan yang benar
		if (Dtrain[x][5] == T):
			betul=betul+1
		
		# menghitung untuk menentukan K terbaik
		akurasi = (betul/200)*100
		if (akurasi > terbaik):
			terbaik=k
		k=k+2

print("K Terbaik = ",terbaik)

# mengapus array yang sudah digunakan sebelumnya 
del hasil[:]
del row_list[:]

# perulangan untuk menebak data uji 
for x in range(len(Duji)):
	hasil=[]
	n0=0
	n1=0
	n2=0
	n3=0
	x1=Duji[x][0]
	x2=Duji[x][1]
	x3=Duji[x][2]
	x4=Duji[x][3]
	x5=Duji[x][4]
	# perulangan sebanyak data latih
	for j in range(len(Dtrain)):
		y1=Dtrain[j][0]
		y2=Dtrain[j][1]
		y3=Dtrain[j][2]
		y4=Dtrain[j][3]
		y5=Dtrain[j][4]
		h= m.sqrt(pow(x1-y1,2) + pow (x2-y2,2) + pow( x3-y3,2) + pow(x4-y4,2) + pow(x5-y5,2))
		row_list=[]
		row_list.append(j)
		row_list.append(h)
		hasil.append(row_list)
	# sort untuk menentukan tetangga terdekat
	hasil.sort(key=lambda p: p[1])
	# perulangan untuk mencari tetangga 
	for z in range(terbaik):
		if(Dtrain[hasil[z][0]][5] == 0):
			n0=n0+1
		elif(Dtrain[hasil[z][0]][5] == 1):
			n1=n1+1
		elif(Dtrain[hasil[z][0]][5] == 2):
			n2=n2+1
		else:
			n3=n3+1
	# kondisi untuk menentukan termasuk kelas yang mana 
	if(n1>n2 and n1>n3 and n1>n0):
		T=1
	elif(n0>n1 and n0>n2 and n0>n3):
		T=0
	elif(n2>n1 and n2>n0 and n2 >n3):
		T=2
	else:
		T=3
	# memasukan data ke array 
	tebak.append(T)
	del hasil[:]
	del row_list[:]
# memindahkan data ke csv 
a= num.asarray(tebak)
num.savetxt("TebakanTugas3.csv",a,delimiter=",", fmt='%10.5f')
