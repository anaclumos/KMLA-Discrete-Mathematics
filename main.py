dataForPartition = []
dataForSet = []

for x in range(100):
	arr1 = []
	arr2 = []
	for y in range(100):
		arr1.append(0)
		arr2.append(0)
	dataForPartition.append(arr1)
	dataForSet.append(arr2)

def C(a, b):
	ans = 1
	div = 1
	for x in range(b):
		ans *= (a-x)
		div *= (x+1)
	return int(ans/div)

def insertp(n, k, value):
	dataForPartition[n][k] = value

def insertS(n, k, value):
	dataForSet[n][k] = value

def p(n, k):
	if n < k:
		return 0

	if dataForPartition[n][k] != 0:
		ans = dataForPartition[n][k]
		print("remember : p(" + str(n) + ", " + str(k) + ") is " + str(ans))
	else:
		if n == k:
			ans = 1
		elif k == 1:
			ans = 1
		elif k == n-1:
			ans = 1
		elif k == n-2:
			ans = 2
		else:
			ans = p(n-1, k-1) + p(n-k, k)
		print("calculate: p(" + str(n) + ", " + str(k) + ") is " + str(ans))
		insertp(n, k, ans)
	return ans

def S(n, k):
	if n < k:
		ans = 0
	if dataForSet[n][k] != 0:
		ans = dataForSet[n][k]
		print("remember : S(" + str(n) + ", " + str(k) + ") is " + str(ans))
	else:	
		if n == k:
			ans = 1
		elif k == 1:
			ans = 1
		elif k == n-1:
			ans =  C(n, 2)
		elif k == n-2:
			ans = C(n, 3) + int(C(n, 2) * C(n-2, 2)/2)
		else:
			ans = S(n-1, k-1) + k * S(n-1, k)
		print("calculate: S(" + str(n) + ", " + str(k) + ") is " + str(ans))
		insertS(n, k, ans)
	return ans

while(True):
	print()
	try:
		n = int(input("n: "))
	except ValueError:
		print("Wrong Input!")
		continue
	try:
		k = int(input("k: "))
	except ValueError:
		print("Wrong Input!")
		continue

	print()
	pVal = p(n, k)
	print()
	sVal = S(n, k)
	print()
	print("p("+str(n)+", "+str(k)+") is", pVal)
	print("S("+str(n)+", "+str(k)+") is", sVal)
