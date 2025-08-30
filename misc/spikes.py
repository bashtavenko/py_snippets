"""Find spikes.
"""


def find_spikes(data):
    sizes = []

    if len(data) < 2:
        return []

    count = 1
    started = False
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            started = True
            count += 1
        elif count > 1:
            sizes.append(count)
            count = 1
            started = False

    if i==len(data) - 1 and started:
        sizes.append(count)

    return sizes
