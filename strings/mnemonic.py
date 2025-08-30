"""6.7 Compute all mnemonic for a phone number."""

# Unmutable tuple
MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')


def phone_mnemonic(phone_number):
    """Returns list combinations for a given phone number.
        2 =>  ['A', 'B', 'C']
        23 => ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
    """
    def mnemonic_helper(digit):
        if digit == len(phone_number):
            # ['A','D'] => 'AD'
            result.append(''.join(partial_result))
        else:
            # Try all possible characters for this digit
            for c in MAPPING[int(phone_number[digit])]:
                partial_result[digit] = c # Since list is prebuilt
                mnemonic_helper(digit + 1)

    # Have function-level buffer for recursion results instead of passing it in.
    # This is a list of phone number length: ['0'], ['0', '0']
    result, partial_result = [], [0] * len(phone_number)
    mnemonic_helper(0)
    return result
