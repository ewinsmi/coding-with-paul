def getMinNum( size ):
	i = 1
	num = "1"
	while i < size:
		num = num + "0"
		i = i + 1
	return int( num )

assert getMinNum( 2 ) == 10
assert getMinNum( 3 ) == 100

def getMaxNum( size ):
	i = 0
	num = ""
	while i < size:
		num = num + "9"
		i = i + 1
	return int( num )

assert getMaxNum( 2 ) == 99
assert getMaxNum( 3 ) == 999

def isPalindrome( n ):
  numAsString = str(n)
  isPalindrome = True
  if len( numAsString ) % 2 != 0:
    return False  # odd length so cannot be a palindrome
  for i in range( 0, len( numAsString )/2 ):
    if numAsString[ i ] != numAsString[ len(numAsString) - 1  - i ]:
      return False
  return True

assert isPalindrome( 1001 )
assert isPalindrome( 123456789987654321 )
assert isPalindrome( 1002 ) == False
assert isPalindrome( 101 ) == False

def findLargestPalindromeMinFirst( size ):
	minNum = getMinNum( size )
	maxNum = getMaxNum( size )
	i = minNum
	largestPalindrome = 0
	while i <= maxNum:
		j = minNum
		while j <= maxNum:
			result = i * j
			if result > largestPalindrome and isPalindrome( result ):
				largestPalindrome = result
			j = j + 1
		i = i + 1
	return largestPalindrome

assert findLargestPalindromeMinFirst( 2 ) == 9009

def debug( *argv ):
	if True:
		print "debug ",
		for arg in argv:
			print str(arg),
		print( " " )

def findLargestPalindromeMaxFirst( size ):
	minNum = getMinNum( size )
	maxNum = getMaxNum( size )
	i = maxNum
	largestPalindrome = 0
	count = 0
	while i >= minNum:
		j = maxNum
		if largestPalindrome != 0 and i*maxNum < largestPalindrome:
			debug( "exit", count )
			return largestPalindrome;
		while j >= minNum:
			count = count + 1
			result = i * j
			if result > largestPalindrome and isPalindrome( result ):
				largestPalindrome = result
				debug( "new palindome", count, i, j, largestPalindrome )
				break;
			elif largestPalindrome != 0 and result < largestPalindrome:
				break;
			j = j - 1
		i = i - 1
	debug( "return", count )
	return largestPalindrome

assert findLargestPalindromeMaxFirst( 2 ) == 9009

print( findLargestPalindromeMaxFirst( 5 ) )