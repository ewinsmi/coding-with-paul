# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the 
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all 
# of the numbers from 1 to 20?
import sys

def gcd(a, b):
  while b:      
    a, b = b, a % b
  return a

assert gcd(2,3), 1 
assert gcd(2,6), 2 
assert gcd(3,15), 3

def lcm( a, b ):
  return a * b // gcd(a, b)

assert lcm(5,15), 5
assert lcm(6,24), 6
assert lcm(6,21), 3

def calculate(num, current_lcm = 1):
  if (num == 1):
    return current_lcm
  return calculate( num - 1, lcm( num, current_lcm ) )

assert calculate(10), 2520

result=calculate(20)
print(result)