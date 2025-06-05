from time import perf_counter_ns


def time_execution(fn):
    def wrapper() -> None:
        start = perf_counter_ns()
        fn()
        elapsed_ms = (perf_counter_ns() - start) / 1_000_000
        print(f"--- elapsed: {elapsed_ms} ms ---")

    return wrapper
