def isPrimeFactor( number, prime ):
  return number % prime == 0

assert isPrimeFactor( 13, 3 ) == False
assert isPrimeFactor( 13, 13 ) == True

def largestPrimeFactor(initialInput):

	#make initial assertions
	assert(initialInput > 0), "initial input must be > 0"
	assert(isinstance(initialInput, int)), "initial input must be whole number"

	#set initial assumptions
	largestPrime = initialInput
	value = 2
	while value * value < largestPrime:
		while isPrimeFactor( largestPrime, value ):
			largestPrime = largestPrime / value
			#print(largestPrime)
		value = value + 1
		#print(value)

        
	assert(int(largestPrime) <= int(initialInput)), "output must be less than input"
	return int(largestPrime)


print(largestPrimeFactor(600851475143))
print(largestPrimeFactor(13))
