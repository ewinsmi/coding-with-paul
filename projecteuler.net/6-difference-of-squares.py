def startAndEnd(a, f):
  starter = a
  end = f
  listOfNos = range(starter, end + 1)
  sumOfList = sum(listOfNos)
  squareOfSum = sumOfList ** 2
  return squareOfSum
  
assert startAndEnd(1,3), 36
assert startAndEnd(4,6), 225 

def squareThisList(list):
  return [i ** 2 for i in list]
  
assert squareThisList((2,3,4)), (4,9,16)
assert squareThisList((5,6,7)), (25,36,49)

def startAndEndSquares(c, d):
  starterSquared = c
  endSquared = d
  listOfNosSquared = range(starterSquared, endSquared + 1)
  squareForList = squareThisList(listOfNosSquared)
  sumOfListSquared = sum(squareForList)
  return sumOfListSquared
  
assert startAndEndSquares(1,3), 14
assert startAndEndSquares(3,5), 50
  
def differenceOfSquares(x, y):
  listSum = startAndEnd(x, y)
  squareOfList = startAndEndSquares(x, y)
  difference =  listSum - squareOfList
  return difference 
  
assert differenceOfSquares(1, 10), 385
  
print(differenceOfSquares(1, 100))


