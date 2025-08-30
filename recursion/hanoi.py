"""15.1 Tower of Hanoi."""

def compute(num_rings):
    def compute_step(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move > 0:
            compute_step(
                    num_rings_to_move - 1, from_peg, use_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            print ('Move from peg {} to peg {}'.format(from_peg, to_peg))
            compute_step(
                    num_rings_to_move - 1, use_peg, to_peg, from_peg)


    NUM_PEGS = 3
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]
    compute_step(num_rings, 0, 1, 2)
