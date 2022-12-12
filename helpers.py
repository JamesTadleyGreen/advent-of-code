import timeit


def timer(func, number_of_runs: int = 1000):
    time = 1
    main_start = timeit.default_timer()
    for _ in range(number_of_runs):
        start = timeit.default_timer()
        func()
        end = timeit.default_timer()
        if (t := (end - start)) < time:
            time = t
    main_end = timeit.default_timer()
    return f"Function `{func.__name__}` took {((main_end - main_start)/number_of_runs)*1_000_000:.1f} microseconds to run on average, with a min time of {time*1_000_000:.1f} microseconds."
