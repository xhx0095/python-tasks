from functools import wraps
import time
def default_timer(func): 
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration_time = end_time - start_time
        print("the function running time is %s: %.2f s" % (func.__name__, duration_time))
        return result
 
    return wrapper
class timer(object):
    def __enter__(self):
        self.t0 = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print ('[the function spent time: {time:.2f}s]'.format(time = time.time() - self.t0))


with timer ():
     print ( sum ( range ( 1000 ) ) )  

@default_timer  
def some_function ():
    return sum ( range ( 1000000 ) )

result = some_function ()
print(result)
