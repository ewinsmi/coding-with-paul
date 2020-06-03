<<<<<<< HEAD
def nth_prime(n):
    counter = 2
    max = n**2
    for i in range(3, max, 2):
        k = 1
        while k*k <i:
            k += 2
            if i % k == 0:
                break
            else:
                counter += 1
            if counter == n:
                return i
assert nth_prime(3), 5
assert nth_prime(6), 13
print('hello')
=======
# By listing the first six prime numbers: 2, 3, 5, 7, 11, 
# and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

# if we used this we could write nth_prime first
def initialisPrime(n):
    if n in [2,3,5,7,11,13,17,19,23,29]: return True
    return False

assert initialisPrime( 24 ) == False
assert initialisPrime( 13 ) == True

# worker function that we need to solve the problem
def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False
    return True

# test data that we know to be true
assert isPrime( 24 ) == False
assert isPrime( 13 ) == True

def nth_prime( n ):
    counter = 0
    i = 0
    while True:
        if isPrime( i ):
            counter = counter + 1
        if counter == n:
            return i
        i = i + 1

# test data from the original question
assert nth_prime(1) == 2
assert nth_prime(3) == 5
assert nth_prime(5) == 11
assert nth_prime(6) == 13

print( nth_prime( 10001 ) )
>>>>>>> 74c7132d6e7eb103648a6adb4ece80b25903ecc4
