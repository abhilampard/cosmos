def getKeyMatrix(key):
	
	matrix = [[None for _ in range(5)]for _ in range(5)]
	used = []
	i=0

	for k in key:

		if k == 'j': k='i'

		if k not in used:
			matrix[int(i/5)][i%5] = k
			used.append(k)
			i += 1

	ascii = ord('a')
	while i < 25:
		c = chr(ascii)
		if c not in used and c is not 'j':
			matrix[int(i/5)][i%5] = c
			i += 1
		ascii += 1

	return matrix

def processMsg(msg):
	
	msg = list(msg.replace(' ','').lower().replace('j','i'))
	mLen = len(msg)

	i=0
	while i+1 < mLen:
		if msg[i] == msg[i+1]: msg.insert(i+1,'x')
		i += 2

	mLen = len(msg)
	if mLen%2 !=0 : msg.append('x')

	return ''.join(msg)

def find(c,matrix):
	
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if matrix[i][j] == c:
				return (i,j)

def encrypt(key,msg):

	msg = list(processMsg(msg))
	keyMatrix = getKeyMatrix(key)

	mLen = len(msg)
	i =0

	while i<mLen:

		r1,c1 = find(msg[i],keyMatrix)
		r2,c2 = find(msg[i+1],keyMatrix)

		if r1 == r2:
			r=r1
			msg[i] = keyMatrix[r][(c1+1)%5]
			msg[i+1] = keyMatrix[r][(c2+1)%5]
		elif c1 == c2:
			c=c1
			msg[i] = keyMatrix[(r1+1)%5][c]
			msg[i+1] = keyMatrix[(r2+1)%5][c]
		else :
			msg[i] = keyMatrix[r1][c2]
			msg[i+1] = keyMatrix[r2][c1]
		i += 2
	return ''.join(msg)

def decrypt(key,msg):

	msg = list(processMsg(msg))
	keyMatrix = getKeyMatrix(key)

	mLen = len(msg)
	i =0

	while i<mLen:

		r1,c1 = find(msg[i],keyMatrix)
		r2,c2 = find(msg[i+1],keyMatrix)

		if r1 == r2:
			r=r1
			msg[i] = keyMatrix[r][(c1-1)%5]
			msg[i+1] = keyMatrix[r][(c2-1)%5]
		elif c1 == c2:
			c=c1
			msg[i] = keyMatrix[(r1-1)%5][c]
			msg[i+1] = keyMatrix[(r2-1)%5][c]
		else :
			msg[i] = keyMatrix[r1][c2]
			msg[i+1] = keyMatrix[r2][c1]
		i += 2
	return ''.join(msg)

key = input('Enter key : ')
msg = input('Enter Msg : ')
cipher = encrypt(key,msg)
print('\nCipher text = ',cipher)
msg = decrypt(key,cipher)
print('\nDecrypted Text = ',msg)
