#计算时间函数  
import time
def print_run_time(func):  
    def wrapper(*args, **kw):  
        local_time = time.time()  
        func(*args, **kw) 
        print('Function [%s] run time is %.2f秒' % (func.__name__ ,time.time() - local_time))
    return wrapper 