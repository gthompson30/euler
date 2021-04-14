import math

'''
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

OUR ALGORITHM:
Our first thought was that the smallest number to be divisible by all numbers 1-20 could just be 20!, all
numbers 1-20 multiplied together. While that would be a number that would be divisible by numbers 1-20, we
quickly realized that was not the smallest. For example, you didn't need the '2' in 1*2*3*4*5...20, because
if any number is divisible by 20, or 10, or any other even number, it is necessarily divisible by 2.

Instead, we broke up every factor in 20! into its prime factors. So,

1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20

became

1 * 2 * 3 * (2 * 2) * 5 * (2 * 3) * 7 * (2 * 2 * 2) * (3 * 3) * (2 * 5) * 11 * (2 * 2 * 3) * 13 * (2 * 7) *
(3 * 5) * (2 * 2 * 2 * 2) * 17 * (3 * 3 * 2) * 19 * (2 * 2 * 5)

These factors could then be reorganized into: 2^18 * 3^8 * 5 * 7 * 11 * 13 * 17 * 19

We originally thought that we could remove the exponents to remove duplicate prime factors, so the
aforementined expression could be turned into:

2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

However, this expression was not divisible by numbers such as 9, 12, 18, and 20, because there aren't enough
2's and 3's as factors to form numbers like 3*3, 2*2*3, 3*3*2, and 2*2*5. To find the lowest common multiple
for the numbers, we would need to find the minimum number of 2's, 3's, 5's, and every other prime for all
numbers to be formed.

We found that the number in 1-20 that required the most 2's was 16, so you would need at least four 2's in
the answer. The number that required the most 3's was a tie between 9 and 18, so two 3's would be needed.
Numbers 5, 7, 11, 13, 17, and 19 are only used once at most in each number 1-20, so they need to only be used
once. So, our final equation would look like:

2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19

This evaluates to 232792560, which is the answer.

In order to write a program to automate this, we realized that we didn't need to count which factors were
repeated the most, because we could just use logarithms.

For the lowest common multiple of numbers 1-20, the number with the most 2's as factors was 16, which was
also a power of two, and moreover, the highest power of two below 20. Knowing that the exponent for any of
the prime numbers was also largest of power of the prime number below 20, we realized that you could just
calculate all of the exponents by taking the floor of the logarithm of 20, with the base being the prime
number. To accomplish this, we used math.log(), from the math module.

In order for this function to work, we also needed to only calculate exponents of prime numbers. To do this,
we created a separate function, is_prime(). is_prime() works by iterating through all numbers from 2 to the
square root of the input, because only numbers up until the square root of a given number are needed to
determine if it's prime. For calculating the primeness of large numbers, this is far more efficient than
iterating from to 2 to n.

In our function, smallest_multiple(n), we take in input n, calculate the minimum 
'''

def is_prime(n):
    if n <= 1:
        return False

    for num in range(2, int(1+((n**.5)//1))):
        if n % num == 0:
            return False
    return True

def smallest_multiple(n):
    sum = 1

    for i in range(1, n+1):
        if is_prime(i):
            sum *= i ** (math.log(n, i) // 1)

    return int(sum)
