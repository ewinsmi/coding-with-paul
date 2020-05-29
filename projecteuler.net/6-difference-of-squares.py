def sumOfRange(starter, end):
  listOfNos = range(starter, end + 1)
  return sum(listOfNos)

def square( value):
  return value ** 2
  
assert sumOfRange(1,3), 6
assert sumOfRange(4,6), 15

def squareThisList(list):
  return [square(i) for i in list]
  
assert squareThisList((2,3,4)), (4,9,16)
assert squareThisList((5,6,7)), (25,36,49)

def squareListThenSum(startOfList, endOfList):
  myList = range(startOfList, endOfList + 1)
  listSquared = squareThisList(myList)
  sumOfSquaredList = sum(listSquared)
  return sumOfSquaredList
  
assert squareListThenSum(1,3), 14
assert squareListThenSum(3,5), 50
  
def differenceOfSquares(x, y):
  listSum = square(sumOfRange(x, y))
  squareOfList = squareListThenSum(x, y)
  difference =  listSum - squareOfList
  return difference 
  
assert differenceOfSquares(1, 10), 385
  
print(differenceOfSquares(1, 100))


