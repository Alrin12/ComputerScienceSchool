from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level = logging.INFO)

    @wraps(orig_func)
    def wrapper_logger(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper_logger

def my_timer(orig_func):
    import time
    @wraps(orig_func)
    def wrapper_time(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() -t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper_time

import time


@my_logger
@my_timer
def ShowInfo(name, age):
    time.sleep(1)
    print('ShowInfo ran with arguments ({}, {})'.format(name, age))

#ShowInfo = my_logger(my_timer(ShowInfo))


ShowInfo('greg', 35)
#ShowInfo('yang', 25)
