prime_number = input("enter number")# user input
"""This funtion determines if the number is a prime number"""
if prime_number> 1:
   for i in range(2,prime_number):
       if (prime_number % i) == 0:
           print(prime_number,"This is not a prime number")
           break
   else:
       print(prime_number,"This is a prime number")
