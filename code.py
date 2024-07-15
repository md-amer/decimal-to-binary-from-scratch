#Decimal to binary from scratch
#By Amer

from time import sleep

def dec_to_bin(n):
	out = []
	while n>0:
		out.append(n%2)
		n = n//2
	output = ''
	for i in out[::-1]:
		output = output + str(i)
	if output == '':
		return 0
	else:
		return int(output)
		
def dots():
	for i in range(2):
		sleep(0.5)
		print('.',end=' ',flush=True)
	sleep(0.5)
	print('.',flush=True)

test = 1

if test == 1:	
	print('Generating Binary numbers',end='')
	dots()
	print()
		
	for i in range(1,1001):
		if i%100 == 0:
			print(str(i) + ': '+str(dec_to_bin(i)))
			print('')
			print('')
			sleep(1)
			
		elif i%10 == 0 and i%100 != 0:
			print(str(i) + ': '+str(dec_to_bin(i)))
			print('')
			sleep(0.5)
			
		else:
			print(str(i) + ': '+str(dec_to_bin(i)))
			sleep(0.1)
