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