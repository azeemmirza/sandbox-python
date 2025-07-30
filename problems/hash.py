import unittest
import random
import string
import pprint
import unittest
import matplotlib.pyplot as plt


# A simple hash function that uses polynomial rolling hash technique.
# This function is designed to minimize collisions for both integers and strings.
def hasher(key: int | str):
  p = 31
  m = 1_000_000_009
  hash_value = 0
  power = 1
  
  if type(key) is int:
    key = str(key)
  
  for c in key:
    hash_value = (hash_value + ord(c) * power) % m
    power = (power * p) % m
  
  return hash_value



# A function to test hash collisions.
# This function generates random integers and strings, hashes them,
# and checks how many collisions occur.
# It uses a simple dictionary to count occurrences of each hash value.
def test_hash_collisions(itr = 100, hashFunc=hasher):
  collision_count = 0
  seen_hashes = {}
  MAX_TOLERANCE = 0.1
  
  
  for _ in range(itr):
    key_type = random.choice(['int', 'str'])
    
    if key_type == 'int':
      key = random.randint(1, 100000)
    else:
      key = ''.join(random.choices(string.ascii_letters, k=10))


    hash_value = hashFunc(key)

    if hash_value in seen_hashes:
      seen_hashes[hash_value] += 1
      collision_count += 1
    else:
      seen_hashes[hash_value] = 1
      
  percentile = collision_count / itr
  
  # print(f'Total collisions: {collision_count}; Percentage: {percentile}')

  return { 'collisions': collision_count, 'percentage': percentile, 'iterations': itr }

# Now plot the data
iterations = [100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

hash_collisions = [
  test_hash_collisions(_, hashFunc=hash)['percentage'] for _ in iterations
  ]

hasher_collisions = [
  test_hash_collisions(_, hashFunc=hasher)['percentage'] for _ in iterations
]

# Plotting the data
plt.figure(figsize=(10,6))

plt.plot(iterations, hash_collisions, label="Python hash() collisions", marker='o')
plt.plot(iterations, hasher_collisions, label="Custom hasher() collisions", marker='o')

plt.xlabel('Number of Iterations')
plt.ylabel('Collision Percentage')
plt.title('Hash Function Collision Percentage Comparison')
plt.legend()

plt.xscale("log")
plt.yscale("log")

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
