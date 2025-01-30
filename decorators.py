
#Timing Decorator : In Python, decorators are special functions that modify other functions without changing their actual code. 
#Think of them like add-ons or filters that can enhance what a function does.
#THIS FILE INCLUDES:
#Measuring performance (timer)
#Logging function calls (logger)
#Improving efficiency (cache)
#Adding delays (delay)




# -----------------Function decorator that times execution-----------------
# What does it do? It measures how long a function takes to run.

# How does it work? The timer decorator records the time before and after the function runs. 
# It then calculates the difference (how long it took to execute) and prints it.

#Why is this useful? It helps you know if a function is too slow and needs optimization.

from time import time
​
def timer(func):
    # Nested wrapper function
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"Duration: {end-start}")
    return wrapper
@timer
def sum_nums():
    result = 0
    for x in range(1000000):
        result += x
​
sum_nums()


#----------------------Logging Decorator----------------------------------
# What does it do? It prints what function is being called, along with its arguments.

#How does it work? The logger decorator prints the function name and the values it was called with before actually running it.

#Why is this useful? It helps track which functions are being called and with what inputs.

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Ran {func.__name__} with args: {args}, and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper
@logger
def add(x, y):
    return x + y
​
@logger
def sub(x, y):
    return x - y
​
add(10, 20)
sub(30, 20)


#--------------------Caching Decorator---------------------------
# What does it do? It saves (caches) results of expensive function calls so they don’t have to be recalculated.

# How does it work? When the function is first called with a specific input, the result is stored.
# If called again with the same input, it returns the stored result instantly.

# Why is this useful? If a function is slow, caching prevents unnecessary re-computation.

import functools
​
def cache(func):
    cache_data = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key not in cache_data:
            cache_data[key] = func(*args, **kwargs)
        return cache_data[key]
    return wrapper
​
import time
@cache
def expensive_func(x):
    start_time = time.time()
    time.sleep(2)
    print(f"{expensive_func.__name__} ran in {time.time() - start_time:.2f} secs")
    return x
​
​
​
%time print(expensive_func(1))
expensive_func ran in 2.00 secs
1
CPU times: user 10.4 ms, sys: 2.82 ms, total: 13.2 ms
Wall time: 2 s
%time print(expensive_func(1))
1
CPU times: user 619 µs, sys: 100 µs, total: 719 µs
Wall time: 725 µs
@cache

##### Fibonacci Example: The cache decorator speeds up recursive functions like Fibonacci by storing results.
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
fibonacci(10)


#---------------------------------Delay Decorator----------------
#What does it do? It makes a function wait before running.

#How does it work? It tells Python to sleep for a certain number of seconds before executing the function.

#Why is this useful? Great for delaying retries or slowing down API calls.

import time
from functools import wraps
​
def delay(seconds):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Sleeping for {seconds} seconds before running {func.__name__}")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return inner
@delay(seconds=3)
def print_text():
    print("Hello World")

print_text()
@delay(seconds=3)
def print_text():
    print("Hello World")
​
print_text()

#-------------IMPROVED TIMER---------------------
#Tracks fastest and slowest execution times for a function.
#logs these durations across multiple calls.

from time import time

def timer(func):
    fastest = float('inf')
    slowest = 0

    def wrapper(*args, **kwargs):
        nonlocal fastest, slowest
        start = time()
        result = func(*args, **kwargs)
        end = time()
        duration = end - start

        fastest = min(fastest, duration)
        slowest = max(slowest, duration)

        print(f"Duration: {duration:.6f} sec | Fastest: {fastest:.6f} sec | Slowest: {slowest:.6f} sec")
        return result
    return wrapper

@timer
def sum_nums():
    return sum(range(1000000))

sum_nums()  # Call multiple times to observe fastest and slowest
sum_nums()

#----------------------Debug DecoratoR---------------------
#Automatically enters Python's debugger (pdb) before function execution.
#Useful for inspecting values before running a function.

import pdb

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Entering debugger before calling {func.__name__}")
        pdb.set_trace()  # Enter interactive debugging mode
        return func(*args, **kwargs)
    return wrapper

@debug
def test_debug(x, y):
    return x + y

# Call function, will enter debugger
# test_debug(5, 10)


#----------------------Retry Decorator -------------------------------

#Retries a function up to max_attempts times if it fails.
#Can be used for functions that randomly fail due to network issues, API calls, etc.

import time
import random

def retry(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempts+1} failed: {e}")
                    attempts += 1
                    time.sleep(delay)
            print(f"Function {func.__name__} failed after {max_attempts} attempts.")
            return None
        return wrapper
    return decorator

@retry(max_attempts=5, delay=2)
def unstable_function():
    if random.random() < 0.7:  # 70% chance of failure
        raise ValueError("Random failure!")
    return "Success!"

# unstable_function()  # Call multiple times to see retries in action

#--------------------------Enhanced Cache with LRU Expiration 
#Implements an LRU (Least Recently Used) cache using functools.lru_cache.
#Limits cache size to avoid memory overuse.

from functools import lru_cache

@lru_cache(maxsize=5)  # Caches up to 5 results
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Caching speeds up repeated calls
print(fibonacci(9))   # Uses cache instead of recalculating


#-----------------------------Parameterized Delay Decorator-------------------
#Allows dynamic delay customization using parameters.

import time
from functools import wraps

def delay(seconds=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Sleeping for {seconds} seconds before running {func.__name__}")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@delay(seconds=3)
def print_text():
    print("Hello, delayed world!")

print_text()  # Will wait 3 seconds before execution

