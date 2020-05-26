def calculate():
    target = 20
    candidate = 1
    success = False
    divisors = range(1, target+1)
    while not success:
        for divisor in divisors:
            if candidate % divisor != 0:
                candidate += 1
                break
        else:
            success = True

    return candidate
    
print(calculate)