def flippingMatrix(matrix):
    n = len(matrix) // 2  # Since the matrix is 2n x 2n, we divide by 2 to find n
    max_sum = 0

    for i in range(n):
        for j in range(n):
            # Each element in the top-left quadrant can be replaced potentially by flipping rows/columns
            # with one of four elements (itself, its mirror in the same row, its mirror in the same column,
            # or its diagonal opposite)
            element_max = max(
                matrix[i][j],  # Original position
                matrix[i][2 * n - j - 1],  # Mirror in the same row
                matrix[2 * n - i - 1][j],  # Mirror in the same column
                matrix[2 * n - i - 1][2 * n - j - 1]  # Diagonal opposite
            )
            max_sum += element_max

    return max_sum