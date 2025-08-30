"""11.9 Missing IP address.

Have a file with 1 billion of IP addresses as 32 bit integer.
Find one missing.
Have unlimited disk space but limited RAM (few megabytes)
"""


def find_missing(ifs):
    NUM_BUCKETS =  1 << 16  # 2 ^ 16
    counter = [0] * NUM_BUCKETS
    for x in map(int, ifs):
        upper_part_x = x >> 16
        counter[upper_part_x] += 1

    # Look for a bucket that contains less than (1 << 16) elements.
    BUCKET_CAPACITY = 1 << 16
    candidate_bucket = next(
        i for i, c in enumerate(counter) if c < BUCKET_CAPACITY)

    # Finds all IP addresses in the stream whose first 16 bits are equal to
    # candidate bucket
    ifs.seek(0)
    bit_vec = [0] * BUCKET_CAPACITY
    for x in map(int, ifs):
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            # Records the presense of 16 LSB of x
            lower_part_x = ((1 << 16) -1) & x
            bit_vec[lower_part_x] = 1

    # At least one of the LSB combinations is absent, find it
    for i, v in enumerate(bit_vec):
        if v == 0:
            return (candidate_bucket << 16) | i

