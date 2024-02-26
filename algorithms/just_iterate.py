import random
import time

import matplotlib.pyplot as plt


# binary search
def binsearch(nums, n):
    lo, hi = 0, len(nums)

    while hi > lo:
        mid = (lo + hi) // 2
        x = nums[mid]
        if x == n:
            return mid
        if n < x:
            hi = mid
        if n>x:
            lo = mid + 1
    return None


def iterative_search(nums, n):
    for i in range(len(nums)):
        if nums[i] == n:
            return i
    return None


def generate_test_case(arr_size):

    nums = []
    for _ in range(arr_size):
        nums.append(random.randint(0, arr_size))

    if random.random() < 0.5:  # n outside array 50% times
        n = -1
    else:
        n = random.choice(nums)  # n is random num in array

    return nums, n


def get_avg_time(fn, test_cases):
    tot_time = 0
    for nums, n in test_cases:
        t0 = time.time()
        fn(nums, n)
        t1 = time.time()
        tot_time += t1-t0
    return {"avg_time": tot_time / len(test_cases), "num_tests": len(test_cases), "tot_time": tot_time}


N_RUNS = 100
outputs_bs = {}
outputs_iter = {}
input_sizes = [s for s in range(5, 100, 10)]
for arr_size in input_sizes:
    test_cases = [generate_test_case(arr_size) for _ in range(N_RUNS)]
    outputs_bs[arr_size] = get_avg_time(fn=binsearch, test_cases=test_cases)
    outputs_iter[arr_size] = get_avg_time(fn=iterative_search, test_cases=test_cases)


x = input_sizes
y_bs = [outputs_bs[i]["avg_time"] for i in input_sizes]
y_it = [outputs_iter[i]["avg_time"] for i in input_sizes]

plt.plot(x, y_bs, label="binary search")
plt.plot(x, y_it, label="iterative search")

plt.xlabel("Input Size")
plt.ylabel("Average Running Time")
plt.legend()
# plt.ylim(0, 0.01)
plt.title('Comparison of Running Times')
plt.show()
# plt.savefig("algorithms/output_files/binsearch_vs_iter.png")
# plt.savefig("algorithms/output_files/binsearch_vs_iter_zoomed.png")
# plt.savefig("algorithms/output_files/binsearch_vs_iter_zoomed2.png")
# plt.savefig("algorithms/output_files/binsearch_vs_iter_10_ms.png")