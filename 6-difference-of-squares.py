def startAndEnd(a, f):
  starter = a
  end = f
  listOfNos = range(starter, end + 1)
  sumOfList = sum(listOfNos)
  squareOfSum = sumOfList ** 2
  return squareOfSum

def squareThisList(list):
  return [i ** 2 for i in list]

def startAndEndSquares(c, d):
  starterSquared = c
  endSquared = d
  listOfNosSquared = range(starterSquared, endSquared + 1)
  squareForList = squareThisList(listOfNosSquared)
  sumOfListSquared = sum(squareForList)
  return sumOfListSquared
  
def differenceOfSquares(x, y):
  listSum = startAndEnd(x, y)
  squareOfList = startAndEndSquares(x, y)
  difference =  listSum - squareOfList
  return difference 
  
print(differenceOfSquares(1, 100))
