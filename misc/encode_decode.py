def encode(d):
    header = ",".join([str(len(s)) for s in d])
    return "{}|{}".format(header, "".join(d))


def decode(d):
    result, i, j = [], 0, 0
    parts = d.split("|")
    header = parts[0].split(",")
    for list_len in header:
        item_length = int(list_len)
        j = i + item_length
        result.append(parts[1][i:j])
        i += item_length
    return result


if __name__=="__main__":
    data = encode(["abc", "de", "xyz"])
    print(data)
    print(decode(data))
