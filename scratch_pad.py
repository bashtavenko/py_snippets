def run(data):
    ch_to_i = {char: i for i, char in enumerate(vocab)}
    i_to_ch = {i: char for i, char in enumerate(vocab)}

    print(ch_to_i)
    print(i_to_ch)

    list = [(i, j) for i in range(2) for j in range(3)]
    print(list)


if __name__=="__main__":
    vocab = "$abcdefghijklmnopqrstuvwxyz"
    print(run(vocab))
