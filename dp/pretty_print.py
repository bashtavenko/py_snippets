"""16.11 The pretty printing problem.

The best way to justify text.

Messiness of single line with b blank characters is b^2.

Greedy fits as many words as possible and it won't work because it does not
spread the words uniformly.

0 1 2 3 4       0 1 2 3 4
a   b   c       a   b
d               c   d
0^2 + 4^2 = 16  2^2 + 2^2 = 8

Start on the last word on the last line
"""

CR = '.n'
SPACE = ' '


def calc_min_messiness(words, line_length):
  # Bottom-up DP to compute optimal messiness
  renaming_blanks = line_length - len(words[0])
  cache = ([renaming_blanks**2] + [float('inf')] * (len(words) - 1))

  for i in range(1, len(words)):
    renaming_blanks = line_length - len(words[i])
    cache[i] = cache[i - 1] + renaming_blanks**2
    for j in reversed(range(i)):
      renaming_blanks -= len(words[j]) + 1
      if renaming_blanks < 0:
        # Not enough space
        break
      first_j_messiness = 0 if j - 1 < 0 else cache[j - 1]
      current_line_messiness = renaming_blanks**2
      cache[i] = min(cache[i], first_j_messiness + current_line_messiness)

  return cache[-1]


def simple_wrap(s, k):
  """Kind of ..."""
  result = []
  cur_s = ''
  for line in s:
    for word in line.split(' '):
      #import pdb; pdb.set_trace()
      if len(cur_s) - len(CR) + len(word) <= k:
        cur_s = SPACE.join([cur_s, word])
      else:
        # Didn't fit
        if not CR in word:
          cur_s += CR
          result.append(cur_s)
          cur_s = word # Goes to next line
        else: # Has CR
          result.append(cur_s)
          cur_s = ''

  return result
