def reverse(chars):
    # also [::-1] or reverse(chars)
    # ~i => -i - 1
    # Because in Python there can be negative indexing: a[-3]
    if not chars:
        return
    for i in range(len(chars) // 2):
        chars[i], chars[~i] = chars[~i], chars[i]
