primes = []
i = 2
n=10
while len(primes) < n:
	count=0
	for j in range(1,i+1):
		if i%j==0:
			count+=1
			
	if count<=2:
		primes.append(i)
	
	
	i+=1
	
print(primes)