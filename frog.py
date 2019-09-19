import random
from matplotlib import pyplot as plt
import time, datetime

def frog_jmp(n=1000000, spaces=10, seeds=False, everyj=True): #seed for random number seeds from bin file and everyj is to change the seed every jump if false then, seed is changed every iteraion

	#note the spaces varible is tells how many jumps to the other bank and not the amount of leaf pads
	#link to the problem video -----> https://www.youtube.com/watch?v=ZLTyX4zL2Fc&t=71s

	pavg = 0

	if seeds and everyj:
		with open(seeds, "rb") as f:
			for i in range(n):
				pos = 0
				jmp = 0
				while pos < spaces:
					byte = f.read(1)
					random.seed(byte)
					pos = pos + random.randint(1,spaces-pos)
					#print(pos)
					jmp = jmp + 1
				#print(jmp)
				pavg = pavg+jmp

	elif seeds and not everyj:
		with open(seeds, "rb") as f:
			for i in range(n):
				pos = 0
				jmp = 0
				byte = f.read(1)
				random.seed(byte)
				while pos < spaces:
					pos = pos + random.randint(1,spaces-pos)
					#print(pos)
					jmp = jmp + 1
				#print(jmp)
				pavg = pavg+jmp

	else:
		random.seed()
		for i in range(n):
			pos = 0
			jmp = 0
			while pos < spaces:
				pos = pos + random.SystemRandom().randint(1,spaces-pos)
				#print(pos)
				jmp = jmp + 1
			#print(jmp)
			# if jmp > 7:
				#print(jmp)
			pavg = pavg+jmp
	avg = pavg/n
	return (avg)

def coord(frm,to,file,n=1000000):
	tim = []
	start = time.asctime()
	for sp in range(frm,to):
		print(sp)
		sta = time.time()
		yes.append(frog_jmpn(n,spaces=sp))
		sto = time.time()
		xes.append(sp)
		tim.append(sto-sta)
	f = open(file,'w+')
	f.write("PSEUDO RANDOM\n\n\n\n\n[")
	for m in range(len(xes)):
		if m != len(xes)-1:
			f.write(str(xes[m])+',')
		else:
			f.write(str(xes[m]))
	f.write("]\n[")
	for m in range(len(yes)):
		if m != len(yes)-1:
			f.write(str(yes[m])+',')
		else:
			f.write(str(yes[m]))
	f.write("]\n\n\n")
	f.write("spaces --> average\n")
	for i in range(len(xes)):
		if tim[i] < 60:
			sub = tim[i]
		else:
			sub = datetime.timedelta(seconds = tim[i])
		f.write("{} --> {}  time: {}\n".format(xes[i], yes[i],sub))
	f.write("Start: {}\nStop: {}\n\nxes:{}, yes:{}".format(start, time.asctime(),len(xes),len(yes)))
	f.close()


if __name__ == '__main__':
	xes = []
	yes = []
	for x in range(100,1000001,100):
		print(x)
		xes.append(x)
		yes.append(frog_jmp(x,10))
	f= open("sweet","w+")
	f.write("avg vs iteraions")
	for m in range(len(xes)):
		if m != len(xes)-1:
			f.write(str(xes[m])+',')
		else:
			f.write(str(xes[m]))
	f.write("]\n[")
	for m in range(len(yes)):
		if m != len(yes)-1:
			f.write(str(yes[m])+',')
		else:
			f.write(str(yes[m]))
	f.close()
	plt.plot(xes,yes)
	plt.show()