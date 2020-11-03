from collections.abc import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return False
    else:
        while len(data) > 2:
            if data[0] + data[1] != data[2]:
                return False
            data = data[1:]
        return True
