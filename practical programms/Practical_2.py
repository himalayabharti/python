

#function to check n prime or no
def check(n,fac):
    print()
    for i in range(1,n):
        if n%i==0:
            fac+=1

    if fac<=2:
        print(f"{n} is prime number")
        
    
    

def prime_upto_n(n,fac):
    print()
    for i in range(1,n+1):
        fac=1
        for j in range(2,i):
            if i%j==0:
                fac+=1
        if fac<=1:
            print(f"{i} is prime number")
       




        
        

n=int(input("Enter any number: "))
check(n,1)
prime_upto_n(n,1)



primes = []
i = 2
while len(primes) < n:
	count=0
	for j in range(1,i+1):
		if i%j==0:
			count+=1
			
	if count<=2:
		primes.append(i)

	i+=1

print(primes)
		
	    

        


  
