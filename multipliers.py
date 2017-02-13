#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from random import randint

# Solving problem of Addition-chain exponentiation

# The naıve way of computing a value to the power n performs n-1 multiplications.
# A much better algorithm, discussed in some detail in the Foundations of Computer Science course, can involve repeated squaring:
# pow(x, 1) = x         
# pow(x, n) = pow(x*x, n/2) [n even]
#               = x * pow(x*x, (n-1)/2) [odd]
# Even this is not always optimal. For example, it computes a 15 via the sequence x, x2, x3, x6, x7, x14, x15 in 6
# steps while it is possible to use x, x2, x4, x5, x10, x15 and manage in 5 steps.
# Design a program that can be given an integer n and will find (by some form of exhaustive search)
# the smallest number of multiplications that could be used to raise a value to the power n.

# convert positive number 'n' to 'base'
def getInBase(n, base):
  res = []
  while (n > 0):
    res.append(n%base);
    n=int(n/base);
  return res;

# remove excess удуьутеы from sorted list
def removeExcess(lst):
  seen = set()
  seen_add = seen.add
  tmp = [x for x in lst if not (x in seen or seen_add(x))]
  res = []
  idx = len(tmp) - 1;
  while (idx > 0):
    res = [tmp[idx]] + res;
    while (idx > 0) and (res[0] < tmp[idx-1]): idx-=1;
    idx -=1;
  res.append(tmp[0])

  return res

def isEfficient(num):
  return not (3*"0" in bin(num)[2:]);

# Method of 4-base presentation
#
# Number presented as: n = D_K*4^K + D_(K-1)*4^(K-1) + .. + D_1*4 + D_0
# 1. Suppose first steps are 1, 2
# 2. Untill K!=1:
#       Get 2*D_K; 4 * D_K
#       Get 4*D_K + D_(K-1)
#
# Return number of multiplications to raise any number to power 'n'
def getAddChain(n):
  if (n <= 1):
    return 0;
  
  inBaseVal = getInBase(n, 4);
  result = [2, 3];
  
  tmp = inBaseVal[0]
  for idx in reversed(range(1, len(inBaseVal))):
    if (idx > 0):
      for i in range(0, 2):
        result.append(result[-1]*2);
      
    tmp = 4*tmp+inBaseVal[idx-1];
    result.append(tmp);
  
  result = removeExcess(result)
  return len(result);

# Exponentiation by squearing
# Return number of multiplications 
def squearing(n, cnt):
  if (n <= 1):
    return cnt;
  cnt += 1;
  if (n%2 == 0):
    return squearing(n/2, cnt);
  else:
    cnt += 1;
    return squearing((n-1)/2, cnt);

# Get optimal number of multiplications
def getNumOfMultipl(n):
  if (isEfficient(n)):
    return getAddChain(n);
  return squearing(n, 0);
  
# test efficience
TEST_NUMBERS = 10;
MAX_NUMBER = 1000
for i in range (1, TEST_NUMBERS):
  num = randint(0, MAX_NUMBER);
  efficient = getNumOfMultipl(num);
  squear = squearing(num, 0);
  
  if (efficient <= squear):
    print ("YEEA!   Number:", num, "Result: ", efficient, " <= ", squear)
  else:
    print ("OOPS :( Number:", num, "Result: ", efficient, " > ", squear)

print(getNumOfMultipl(999));
print(getNumOfMultipl(15));
