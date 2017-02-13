## Description

Program that calculates the smallest number of multiplications that could be used to raise a value to the power n.

## Example

Improved algorithm of finding number of multiplications:

pow(x, 1) = x         
pow(x, n) = pow(x*x, n/2) [n even]
          = x * pow(x*x, (n-1)/2) [odd]
          
It is not always optimal.
For example, it computes a 15 via the sequence x, x2, x3, x6, x7, x14, x15 in 6 steps
while it is possible to use x, x2, x4, x5, x10, x15 and manage in 5 steps. So the fastest way to calculate number is in 5 steps.
