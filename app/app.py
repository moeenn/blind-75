from .time_execution import time_execution


@time_execution
def main() -> None:
    print("hello world")
