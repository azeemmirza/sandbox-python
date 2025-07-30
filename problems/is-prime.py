import timeit

'''
This is a simple implementation of a function to check if a number is prime.
The function checks if the number is divisible by any number less than itself.
The time complexity of this function is O(n), where n is the number being checked.
The function can be optimized to O(sqrt(n)) by checking divisibility only up to
the square root of the number.
'''
def is_prime(num: int) -> bool:
  if num == 1 or num == 0:
    return False
  
  res = True
  
  for i in range(num - 1, 1, -1):
    if (num % i == 0):
      res = False
      break
    
  return res
  #end


'''
This is an optimized implementation of a function to check if a number is prime.
It checks if the number is divisible by any odd number starting from 3 up to the number itself, skipping even numbers since they are not prime (except for 2).

The function first checks if the number is 0 or 1, which are not prime.
If the number is 2, it returns True since 2 is the only even prime number
If the number is even and greater than 2, it returns False since all other even numbers are not prime.
Then, it iterates through odd numbers starting from 3 up to the number, checking for divisibility.
'''
def is_prime_fast(num: int) -> bool:
  if num == 1 or num == 0:
    return False
  
  if num == 2:
    return True
  
  if num % 2 == 0:
    return False
  
  for i in range(3, num, 2):
    if num % i == 0:
      return False
  
  return True
  

# Example usage
print(is_prime(2))
print(is_prime_fast(13))

def test_prime_one():
  is_prime(13)
  
def test_prime_two():
  is_prime_fast(13)


# Timing the performance of both implementations
print("Timing results:")
print(timeit.Timer(test_prime_one).timeit(1))
print(timeit.Timer(test_prime_two).timeit(1))