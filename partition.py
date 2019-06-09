data = []

for x in range(100):
	arr = []
	for y in range(100):
		arr.append(0)
	data.append(arr)

def insert(n, k, value):
	data[n][k] = value

def p(n, k):
	if n < k:
		return 0

	if data[n][k] != 0:
		ans = data[n][k]
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
	print("p("+str(n)+", "+str(k)+") is", p(n, k))