import time
import functools


def time_profile(func):
    """Time Profiled for optimisation

   Notes:
        * Do not use this in production

    """

    @functools.wraps(func)
    def profile(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} : {time.time() - start}")
        return result

    return profile
