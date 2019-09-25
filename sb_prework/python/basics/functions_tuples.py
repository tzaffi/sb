# tuples are immutable and like lists


def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)


# keyword args:
print(increment(2, by=3))
print(increment(2))
