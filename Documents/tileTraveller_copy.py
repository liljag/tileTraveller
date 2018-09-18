#Algorithm to win is n n e e s s
import os, sys
def isNorth():
	if((y == 1 or y==2 or (y == 2 and x!=2))and y<4):
		N = True
	else:
		N = False
	return N

def isSouth():
	if(y == 3 or y == 2 or (y==2 and x!=3)):
		S = True
	else:
		S = False
	return S

def isEast():
	if(x==1 or x==2 or (x==2 and y != 2) and (x==1 and y!=1) and (x==2 and y!=1)):
		E = True
	else:
		E = False
	return E

def isWest():
	if((x==2 and y == 2) or ((x==2 or x==3) and y==3)):
		W = True
	else:
		W = False
	return W

def direction(choice, x, y):
	if(d.lower() == 'n' and N==True):
		y+=1
	elif(d.lower() == 's' and S==True):
		y-=1
	elif(d.lower() == 'e' and E==True):
		x+=1
	elif(d.lower() == 'w' and W==True):
		x-=1
	else:
		print("Not a valid direction!")
	return x, y

x, y = 1, 1
print("You can travel: (N)orth.")
N = True
S = True
E = False
W = False
win = False
while(win == False):
	d = raw_input("Direction: ")
	string = ''
	direction(d, x, y)
	W=isWest()
	N=isNorth()
	E=isEast()
	S=isSouth()
	
	
	
	if(x==3 and y==1):
		win = True
	if(d == 'q'):
		win = True
	if(N == True):
		string = string+ '(N)orth'
		if(E==True):
			string = string + ' or (E)ast'
		if(S==True):
			string=string+ ' or (S)outh'
		if(W==True):
			string = string+ ' or (W)est'
	elif(E==True):
		string = string+'(E)ast'
		if(S==True):
			string=string+ ' or (S)outh'
		if(W==True):
			string = string+ ' or (W)est'
	elif(S==True):
		string = string+ '(S)outh'
		if(W==True):
			string = string+ ' or (W)est'
	elif(W==True):
		string=string+ '(W)est'
	
	print("You can travel: "+string)
	#print("You can travel: {0}".format(["(N)orth"]))
print('done')