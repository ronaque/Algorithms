import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func_return = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken to execute the algorithm: {end - start} seconds")
        return func_return
    return wrapper
