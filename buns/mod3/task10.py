def transpone(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


if __name__ == "__main__":
    n = int(input())
    matrix=[]
    [matrix.append([j for j in range(1,n+1)]) for _ in range(1, n+1)]
    [print(line) for line in matrix]
    print()
    [print(line) for line in transpone(matrix)]