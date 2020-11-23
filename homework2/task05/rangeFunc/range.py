"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""
import string


def custom_range(obj, *args):
    result = []
    start = 0
    end = 0
    step = 1
    if len(args) == 1:
        end = obj.index(args[0])
    if len(args) == 2:
        start = obj.index(args[0])
        end = obj.index(args[1])
    if len(args) == 3:
        step = args[2]
        start = obj.index(args[0])
        end = obj.index(args[1])
    for i in range(start, end, step):
        result.append(obj[i])
    return result


print(custom_range(string.ascii_lowercase, "g"))
print(custom_range(string.ascii_lowercase, "g", "p"))
print(custom_range(string.ascii_lowercase, "p", "g", -2))
