class HashTable:
  def __init__(self, size):
    self.size = size
    # creating an array of size with None filled.
    self.table = [None] * size 
  
  
  def _hash(self, key: int | str):
    if type(key) == str:
      key = sum(ord(c) for c in key)
    
    return key % self.size
  
  
  def _probe(self, index):
    original_index = index
    
    while self.table[index] is not None:
      index = (index + 1) % self.size
      
      if index == original_index:
        raise Exception('Hash table is full')
    
    return index
  
  
  def _rehash(self, index = 0):
    next_index = (index + 1) % self.size
    
    while self.table[next_index] is not None:
      s_key, s_value = self.table[next_index]
      self.table = None
      self.insert(s_key, s_value)
      next_index = (index + 1) % self.size
    
    return
  
  
  def insert(self, key, value):
    index = self._hash(key)
    
    if index in self.table:
      index = self._probe(key)
    
    self.table[index] = (key, value)
    
    return
  
  
  def delete(self, key):
    index = self._hash(key)
    original_index = index
    
    while self.table[index] is not None:
      stored_key, v = self.table[index]
      
      if key == stored_key:
        self.table[index] = None
        self._rehash(index)
        return True
      
      index = (index + 1) % self.size
      
      if index == original_index:
        break
    
    return False
  
  
  def put(self, key, value):
    index = self._hash(key)
    original_index = index
    
    while self.table[index] is not None:
      
      if self.table[index][0] == key:
        self.table[index] = (key, value)
        
        return True
      
      index = (index + 1) % self.size
      
      if index == original_index:
        raise Exception('Hash Table is full')
    
    return False
  
  def get(self, key):
    index = self._hash(key)
    
    while self.table[index] is not None:
      if self.table[index][0] == key:
        return self.table[index][1]
      
      index = (index + 1) % self.size
    
    return None
  
  def __str__(self):
    return ''.join(f'\n{e[0]} : {e[1]}' for e in self.table if e is not None)
  
  
  

# Testing the HashTable with Linear Probing

ht = HashTable(size=10)

# Insert key-value pairs
ht.insert("name", "John")
ht.insert("age", 25)
ht.insert("city", "New York")

# Retrieve values
print("Name:", ht.get("name"))  # Output: John
print("Age:", ht.get("age"))    # Output: 25
print("City:", ht.get("city"))  # Output: New York

# Delete a key-value pair
ht.delete("age")
print("Age after deletion:", ht.get("age"))  # Output: None

# Display the table
print("Hashtable:", ht)