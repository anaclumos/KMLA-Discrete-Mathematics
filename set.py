data = []

for x in range(100):
	arr = []
	for y in range(100):
		arr.append(0)
	data.append(arr)

def insert(n, k, value):
	data[n][k] = value

def C(a, b):
	ans = 1
	div = 1
	for x in range(b):
		ans *= (a-x)
		div *= (x+1)
	return int(ans/div)

def S(n, k):
	if n < k:
		ans = 0
	if data[n][k] != 0:
		ans = data[n][k]
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
		insert(n, k, ans)
	return ans

while(True):
	print()
	try:
		n = int(input("n: "))
	except ValueError:
		print("Wrong Input!")
		continue
	if n == "end":
		break
	try:
		k = int(input("k: "))
	except ValueError:
		print("Wrong Input!")
		continue
	if k == "end":
		break
	print("S("+str(n)+", "+str(k)+") is", S(n, k))
