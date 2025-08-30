
def decompress(compressed):
    """
    Decompresses string given a compressed string with magic three-tuple consisting
    of 0XFE-length-offset. Offset is zero-based from the current position in the
    decompressed string.
    Args:
        compressed: compressed string
    Returns:
        Decompressed string
    """
    out = ''
    ci = 0
    while ci < len(compressed) - 1:
        if compressed[ci] == '\xFE':
            length, offset = int(compressed[ci + 1]), int(compressed[ci + 2])
            start = len(out) - offset - 1
            stop = start + length
            out += out[start:stop]
            ci += 3
        else:
            out += compressed[ci]
            ci += 1
    return out
