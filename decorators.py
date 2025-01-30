
Timing Decorator
# Function decorator that times execution
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
Duration: 0.05103158950805664
Logging Decorator
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
Ran add with args: (10, 20), and kwargs: {}
Ran sub with args: (30, 20), and kwargs: {}
10
Caching Decorator
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
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
fibonacci(10)
55
Delay
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
Sleeping for 3 seconds before running print_text
Hello World
