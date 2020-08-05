
# Making a linked list vs. just iterating down: how do you want to implement your hashtable?
## Option 1: create a LL class, or import it, and HashTable class calls the LL methods
## Option 2: inside your HashTable class, make your put/get/delete iterate down the nodes

# Resizing
## What does the OS do if your array gets filled up?
### Find a new spot in memory - double the size of the old one
### Copy old array into new one
### Return the address in memory of your new array


## if hash table is 70% full, how long does the next put take?
### O(n) where n is number of items in hash table

## put takes constant time, if we amortize out the cost of resizing


## compare to dropping the small terms in big O?
### O(n^2)

def quadratic(array):
    for x in array: # million
        print(x)
    
    for x in array: # million * million
        for y in array:
            print(x, y)
        

# Hashing Functions Uses
## Hash a key and work with a hash table
## Use with a database
## Encryption
### Hashing a password
### authentication
##### We want a slow hash function, to prevent brute force

def my_password_hash_function():
    pass


## Encryption - cryptography
### the output often called digest, the hash
"The quick brown fox jumped over the lazy dog \n and then went to sleep \n shall i compare thee"
### 0x1ad4fe598373cb
### MD5, SHA256

### Tweet the hash
#### Proves the document existed at some time
#### Produce a work of art
#### ....or code
#### Scientific discovery, or patent


# What if we used SHA256, which never produces collisions? Does our hash table need to handle collisions?
## Still have collisions, because we modulo the output with our hash table length

----------------------------------------------------------------------
# fibonacci sequence?
## the next number is sum of previous 2
## 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

# base case
# progress toward the base case
# call itself

# memoize in a cache?
cache = {}

def fib(n):
    # base case
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)

    return cache[n]

# O(2^n)
# O(times_calls_self^n)

print(fib(40))

# memoization
# dynamic programming
-------------------------------------------------------------------


# Resizing an array is linear
# Pre-allocating is one option
my_arr = [None] * 100000000

# Pre-populate your cache
import math

def inverse_root(num):
    return 1 / math.sqrt(num)

    
cache = {}   

def populate_cache():
    for i in range(1, 1000):
        cache[i] = inverse_root(i)

populate_cache()

print(inverse_root(999))
print(cache[999])



# Lazy computation
# Lazily computed




    
# Hash table:
## Hash function
## Backed by an array
## Some way to handle collisions: Linked list (or use open addressing)

# Dictionaries and objects are just hash tables with a few methods added
## you could add a .items(), .values()

-----------------------------------------------------------

# If you iterate across, or print a hash table, will the items be in the order in which you put them?
## No
## Why not?
### sets and objects are not ordered
## Unlike lists/arrays

## Python dictionaries do preserve order


# Sorting
my_list = [99, 45, 12, 67, 23, 5]
# sorted, list.sort()

# basically hash table with methods added
mydict = {"foo": 11, "bar": 42, "qux": 99}

# it doesn't make sense to sort a hash table
# sort a list based on the dictionary

# lambda functions are much like anonymous functions in JS
# JS: (x) => x[1] in js

# sorted takes key=lambda, uses what the anonymous function returns to sort

# use lambda function to sort by value
# sorted(my_items, key=lambda x: x[1])

my_dict_items = list(mydict.items())

# sort by value
my_dict_items.sort(key=lambda x: x[1])

# sort by value, descending order
my_dict_items.sort(key=lambda x: x[1], reverse=True)