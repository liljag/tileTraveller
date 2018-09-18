#Algorithm to win is n n e e s s
#https://github.com/liljag/tileTraveller
#1. Implementing with functions was easier becauseit compartmentalizes
#	each part and makes it easier to read and edit
#2. Again, the one with functions is more readable for me because
#	it spaces it out and puts it into sections
#3. There werent any problems with the first implementation so with
#	this implementation there wasnt much it could help me fix aside
#	from decluttering

def string():
	string = ''
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
	string = string +'.'
	return string

def isNorth(x, y):
	if(y == 1 or (y==2 and (x==1 or x==3))):
		N = True
	else:
		N = False
	return N

def isSouth(x, y):
	if((y == 3 and (x==1 or x==3)) or y == 2):
		S = True
	else:
		S = False
	return S

def isEast(x, y):
	if((x==1 and (y==2 or y==3)) or (x==2 and y==3) or (x==1 and y!=1)):
		E = True
	else:
		E = False
	return E

def isWest(x, y):
	if((x==2 and y == 2) or ((x==2 or x==3) and y==3)):
		W = True
	else:
		W = False
	return W

def direction(x, y):
	valid = True
	while(valid):
		d = input("Direction: ")
		if(d.lower() == 'n' and N==True):
			y+=1
			valid = False
		elif(d.lower() == 's' and S==True):
			y-=1
			valid = False
		elif(d.lower() == 'e' and E==True):
			x+=1
			valid = False
		elif(d.lower() == 'w' and W==True):
			x-=1
			valid = False
		else:
			print("Not a valid direction!")
	return x, y

x, y = 1, 1
#print("You can travel: (N)orth.")
N = True
S = False
E = False
W = False
win = False
while(win == False):
	prent = string()
	print("You can travel: "+prent)
	x, y = direction(x, y)
	N = isNorth(x, y)
	S = isSouth(x, y)
	E = isEast(x, y)
	W = isWest(x, y)
	if(x==3 and y==1):
		win = True
	
	#print("You can travel: {0}".format(["(N)orth"]))
print('Victory!')