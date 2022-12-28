import datetime


def timer(func, number_of_runs: int):
    start = datetime.datetime.now()
    [func() for _ in range(number_of_runs)]
    end = datetime.datetime.now()
    return f"Function {func.__name__} took an average of {(end - start)/number_of_runs} to run."
