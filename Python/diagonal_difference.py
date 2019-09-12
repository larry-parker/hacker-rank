def diagonalDifference(arr):
    # Write your code here
    n = len(arr[0])
    indices = [u for u in range(0, n)]
    rd_indices = [i for i in indices]
    # same as reverse of rd_indices
    ld_indices = [n - 1 - i for i in indices]

    right_diagonal = [arr[i][i] for i in rd_indices]
    left_diagonal = [arr[n - 1 - i][i] for i in ld_indices]

    return abs(sum(left_diagonal) - sum(right_diagonal))


dd = diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])

print(dd)
