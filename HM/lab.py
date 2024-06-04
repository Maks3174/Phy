import time
import functools
#1
def count_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return count_paths(m - 1, n) + count_paths(m, n - 1)

m = 3
n = 3
print("Кількість можливих шляхів:", count_paths(m, n))

#2
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Function executed in {run_time:.4f} seconds")
        return value
    return wrapper_timer

@timer
def example_function():
    time.sleep(2)

example_function()


def check_authentication(func):
    user_authenticated = True

    def wrapper_authentication(*args, **kwargs):
        if user_authenticated:
            return func(*args, **kwargs)
        else:
            print("Authentication failed. Access denied.")

    return wrapper_authentication


@check_authentication
def example_function():
    print("Function executed successfully.")


example_function()


def limit_calls(max_calls):
    def decorator(func):
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                print("Function call limit exceeded.")

        return wrapper

    return decorator


@limit_calls(3)
def example_function():
    print("Function executed successfully.")


example_function()
example_function()
example_function()
example_function()