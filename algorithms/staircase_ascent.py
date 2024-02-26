def get_n_ways(n: int, n_ways_dict=None) -> int:
    """
    return the number of ways to climb n stairs
    """
    if n_ways_dict is None:
        n_ways_dict = {}
    if n < 1:
        raise ValueError("n should be greater than 1")
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n in n_ways_dict:
        return n_ways_dict[n]
    n_ways = get_n_ways(n - 1) + get_n_ways(n - 2) + get_n_ways(n - 3)
    n_ways_dict[n] = n_ways
    return n_ways


def get_n_ways_optimized(n: int) -> int:
    """
    return the number of ways to climb n stairs
    """
    prev_prev_prev = 1
    prev_prev = 2
    prev = 4

    if n == 1:
        return prev_prev

    if n == 2:
        return prev

    if n < 1:
        raise ValueError("n should be greater than 1")

    for i in range(4, n + 1):
        n_ways = prev + prev_prev + prev_prev_prev
        prev_prev_prev = prev_prev
        prev_prev = prev
        prev = n_ways

    return n_ways


# review recursion master theorem. check complexity without memoization ()
n = 10
print(get_n_ways(n))
print(get_n_ways_optimized(n))
