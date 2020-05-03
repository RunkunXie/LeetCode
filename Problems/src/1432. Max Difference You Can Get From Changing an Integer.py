class Solution:

    """online sol, using replace"""
    def maxDiff(self, num: int) -> int:
        a = b = str(num)

        for digit in a:
            if digit != "9":
                a = a.replace(digit, "9")
                break

        if b[0] != "1":
            b = b.replace(b[0], "1")
        else:
            for digit in b[1:]:
                if digit not in "01":
                    b = b.replace(digit, "0")
                    break

        return int(a) - int(b)

    """my sol"""
    def maxDiff(self, num: int) -> int:

        num_str = str(num)
        n = len(num_str)

        if n == 1:
            return 9 - 1

        a = []
        if num_str[0] != '1':
            a.append('1')
            tmp = num_str[0]
            for i in range(1, n):
                if num_str[i] == tmp:
                    a.append('1')
                else:
                    a.append(num_str[i])
                print(a)
        else:
            tmp = None
            a.append('1')
            for i in range(1, n):
                if num_str[i] != '0' and num_str[i] != '1':
                    if not tmp:
                        tmp = num_str[i]
                        a.append('0')
                    elif num_str[i] == tmp:
                        a.append('0')
                    else:
                        a.append(num_str[i])
                else:
                    a.append(num_str[i])
                print(a)

        b = []
        tmp = None
        for i in range(n):
            if num_str[i] != '9':
                if not tmp:
                    tmp = num_str[i]
                    b.append('9')
                elif num_str[i] == tmp:
                    b.append('9')
                else:
                    b.append(num_str[i])
            else:
                b.append(num_str[i])
            print(b)

        return int(''.join(b)) - int(''.join(a))
