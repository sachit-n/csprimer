def binary_search(arr, n, start_ix=0, end_ix=None):
    if end_ix is None:
        end_ix = len(arr) - 1

    mid_ix = (start_ix + end_ix) // 2

    if arr[mid_ix] == n:
        return mid_ix

    if start_ix >= end_ix:
        return max(start_ix, end_ix)

    if arr[mid_ix] > n:
        return binary_search(arr, n, start_ix, mid_ix)
    else:
        return binary_search(arr, n, mid_ix+1, end_ix)  # infinite loop


arr1 = [0, 3, 9, 22, 23]
cases1 = [4, 3, 21, 22]
print(f"For arr {arr1}:)")
for i in range(len(cases1)):
    print(f"{cases1[i]} is in index {binary_search(arr1, cases1[i])}")

arr2 = [-2, 8, 999, 1223, 3453, 103232]
cases2 = [999, 0, 2, 3452, 3453]
for i in range(len(cases2)):
    print(f"For arr {arr2}:\n {cases2[i]} is in index {binary_search(arr2, cases2[i])}")
