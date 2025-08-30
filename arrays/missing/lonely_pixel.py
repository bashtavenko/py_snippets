"""Locate lonely pixel in a binary array."""


def lonely_pixel(image):
    """Finds lonely pixels in a binary array.

    Args:
      image: list of lists with 1/0 being black and while pixel resp.

    Returns: sequence of tuples
    """
    out = []
    for i, row in enumerate(image):  # i - row index
        for j, pixel in enumerate(row):  # j - column index
            if pixel:
                lonely = True
                for n in range(len(image)):  # Check column
                    if image[n][j] and n != i:
                        lonely = False
                        break
                    for p in range(len(image[0])):  # Check row
                        if image[i][p] and p != j:
                            lonely = False
                            break
                if lonely:
                    out.append((i, j))
    return out


def lonely_pixel_with_count(image):
    """Finds lonely pixels in a binary array by counting.

    Args:
      image: list of lists with 1/0 being black and while pixel resp.

    Returns: sequence of tuples
    """
    col_count = [0] * len(image[0])
    row_count = [0] * len(image)
    for i, row in enumerate(image):
        row_count[i] = sum(row)
        for j, pixel in enumerate(row):
            col_count[j] += pixel

    out = []
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == 1 and col_count[j] == 1 and row_count[i] == 1:
                out.append((i, j))
    return out
