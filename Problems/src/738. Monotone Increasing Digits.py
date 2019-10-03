class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:

        # turn to digits
        N_digits = [int(n) for n in str(N)]
        count = 0

        # three situations
        for i, n in enumerate(N_digits[:-1]):

            # 1. if current digit n < N_digits[i+1], save it
            if n < N_digits[i + 1]:
                count = 0

            # 2. if current digit n == N_digits[i+1], count it
            elif n == N_digits[i + 1]:
                count += 1

            # 3. if current digit n > N_digits[i+1], reduce by 1, append 9's, break
            else:
                N_digits[i - count] -= 1
                for j in range(i - count + 1, len(N_digits)):
                    N_digits[j] = 9
                break

        # generate result
        return int(''.join([str(n) for n in N_digits]))

N = 12345
N = 543
N = 553
N = 10
