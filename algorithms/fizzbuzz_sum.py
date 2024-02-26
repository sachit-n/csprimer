def get_fizbuzz_sum(n: int) -> int:
    num_div_by3 = (n-1) // 3
    num_div_by5 = (n - 1) // 5
    num_div_by15 = (n - 1) // 15

    sum_of_3s = 3*num_div_by3*(num_div_by3+1) / 2
    sum_of_5s = 5*num_div_by5*(num_div_by5+1) / 2
    sum_of_15s = 15 * num_div_by15 * (num_div_by15 + 1) / 2

    return int(sum_of_3s + sum_of_5s - sum_of_15s)

print(get_fizbuzz_sum(1000))


