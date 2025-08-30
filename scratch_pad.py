def run(data):
    def do_diagonal(index_i, index_j):
        while index_j >= 0 and index_i < len(data[0]):
            result.append(data[index_i][index_j])
            index_i += 1
            index_j -= 1

    result = []
    for col in range(len(data)):
        do_diagonal(0, col)
    for row in range(1, len(data)):
        do_diagonal(row, len(data) - 1)
    return result


if __name__=="__main__":
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(run(a))
