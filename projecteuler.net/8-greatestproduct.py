import os

number = "73167176531330624919225119674426574742355349194934"
number += "96983520312774506326239578318016984801869478851843"
number += "85861560789112949495459501737958331952853208805511"
number += "12540698747158523863050715693290963295227443043557"
number += "66896648950445244523161731856403098711121722383113"
number += "62229893423380308135336276614282806444486645238749"
number += "30358907296290491560440772390713810515859307960866"
number += "70172427121883998797908792274921901699720888093776"
number += "65727333001053367881220235421809751254540594752243"
number += "52584907711670556013604839586446706324415722155397"
number += "53697817977846174064955149290862569321978468622482"
number += "83972241375657056057490261407972968652414535100474"
number += "82166370484403199890008895243450658541227588666881"
number += "16427171479924442928230863465674813919123162824586"
number += "17866458359124566529476545682848912883142607690042"
number += "24219022671055626321111109370544217506941658960408"
number += "07198403850962455444362981230987879927244284909188"
number += "84580156166097919133875499200524063689912560717606"
number += "05886116467109405077541002256983155200055935729725"
number += "71636269561882670428252483600823257530420752963450"

def getProduct( myNumber, index, size ):
  myRange = myNumber[index:index+size]
  product = 1
  for j in range( 0, len(myRange) ):
    if myRange[j] == "0":
      return 0
    else:
      product *= int(myRange[j])
  return product

assert getProduct( "123045607890123", 0, 4 ) == 0
assert getProduct( "123045607890123", 0, 3 ) == 6 
assert getProduct( "123045607890123", 4, 3 ) == 120
assert getProduct( "123045607890123", 8, 3 ) == 504 
assert getProduct( "123045607890123", 0, 2 ) == 2
assert getProduct( "123045607890123", 9, 2 ) == 72

def getMaxProduct( myNumber, size ):
  maxProduct = 0
  for i in range( 0, len(myNumber) ):
    product = getProduct( myNumber, i, size )
    if product > maxProduct:
      maxProduct = product
  return maxProduct

assert getMaxProduct( "123045607890", 4 ) == 0
assert getMaxProduct( "123045607890123", 4 ) == 6
assert getMaxProduct( "123045607890999", 4 ) == 729
assert getMaxProduct( "123045607890123", 3 ) == 504
assert getMaxProduct( "123045607890123", 2 ) == 72

def loadLine( line, myNumbers ):
  # remove any whitespace at start and end
  line = line.strip()
  if ( len(line) == 0 ):
    myNumbers.append( "" )
  else:
    pos = len(myNumbers)-1
    myNumbers[ pos ] = myNumbers[ pos ] + line 

def isValidNumber( number ):
  if len( number ) == 0:
    return False
  try:
    string_int = int(number)
  except ValueError:
    return False
  return True

assert isValidNumber( "123045607890123" ) == True
assert isValidNumber( "1230ABC7890123" ) == False

def processNumbers( myNumbers, size ):
  for number in myNumbers:
    if isValidNumber( number ):
      print( getMaxProduct( number, size ) )

def loadAndProcessFile( filename, size ):
  myfile = open( filename, "r" )
  line = myfile.readline()
  loadednumbers = []
  loadednumbers.append( "" )
  while line:
    loadLine( line, loadednumbers )
    line = myfile.readline()
  myfile.close()
  processNumbers( loadednumbers, size )

#print( os.getcwd() )
loadAndProcessFile( 'projecteuler.net/8-sampledata-happypath.txt', 3 )
loadAndProcessFile( 'projecteuler.net/8-sampledata-emptyfile.txt', 3 )
loadAndProcessFile( 'projecteuler.net/8-sampledata-alphanumeric.txt', 3 )
loadAndProcessFile( 'projecteuler.net/8-sampledata-startwithnewline.txt', 3 )
loadAndProcessFile( 'projecteuler.net/8-sampledata-endwithoutnewline.txt', 3 )
# print( getMaxProduct( number, 13 ) )
