check = [1,2,3,5,7,11,13,17,19,20]

def lowestDivisible( numberInput):
	for num in range (numberInput, 999999999, numberInput):
		if all(num % n for n in check):
			return num
	return num

print(lowestDivisible(20))
