primesList = []

def isPrimeFactor( number ):
  if number < 2:
    print("not a prime")
  for i in range(2, number):
    if number % 2 == 0:
      break
    else:
      primesList.append(number)

isPrimeFactor(9999999)

def whichPrimeIsThis(getIndex):
    return primesList[getIndex + 1]

print(whichPrimeIsThis(10001))
