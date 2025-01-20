import time


def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper
#here example_function id decored by timer function when ever expample_function is called it will first execute timer 
@timer  # we not need to call timer function @timer shows that everything from this line will pass from this function
def example_function(n):
    time.sleep(n)

example_function(5)