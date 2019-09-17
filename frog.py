import random

def frog_jmp(n=100000, spaces=10, seeds=False, everyj=True): #seed for random number seeds from bin file and everyj is to change the seed every jump if false then, seed is changed every iteraion

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




if __name__ == '__main__':

	print("Pseudo random: {}".format(frog_jmp()))
	print("Slightly more pseudo random: {}".format(frog_jmp(seeds="file1.bin",everyj=False)))
	print("Most random: {}".format(frog_jmp(seeds="file2.bin")))