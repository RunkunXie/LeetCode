# Q3
class Solution:
    # Q1419
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:

        max_num, rem = divmod(len(croakOfFrogs), 5)
        if rem is not 0:
            return -1

        rec = {i: "" for i in range(max_num + 1)}
        cur_num = 0
        min_num = 0
        next_valid = {c: [] for c in 'roak'}
        next_char = {'croak'[i]: 'croak'[i + 1] for i in range(4)}
        valid_set = set()

        for char in croakOfFrogs:

            while rec[cur_num] != "":
                cur_num += 1

            if char == 'c':
                rec[cur_num] += 'c'

                valid_set.add('r')
                next_valid['r'].append(cur_num)

            elif char in valid_set:
                chg_num = next_valid[char][0]
                rec[chg_num] += char

                next_valid[char] = next_valid[char][1:]
                if len(next_valid[char]) == 0:
                    valid_set.remove(char)

                if char == 'k':
                    rec[chg_num] = ""
                    cur_num = chg_num
                else:
                    valid_set.add(next_char[char])
                    next_valid[next_char[char]].append(chg_num)

            else:
                return -1

            # print(rec, next_valid, valid_set)

            min_num = max(min_num, cur_num)

        return min_num

print(Solution().minNumberOfFrogs("crocakroak"), 2)
print(Solution().minNumberOfFrogs("ccrrooaakk"), 2)
print(Solution().minNumberOfFrogs("croakcrook"), -1)
print(Solution().minNumberOfFrogs("ccrrooaacroacroakkcroakcroakkk"), 4)
print(Solution().minNumberOfFrogs("ccccccccccrrccccccrcccccccccccrcccccccccrcccccccccccrcccccrcccrrcccccccccccccrocrrcccccccccrccrocccccrccccrrcccccccrrrcrrcrccrcoccroccrccccccccorocrocccrrrrcrccrcrcrcrccrcroccccrccccroorcacrkcccrrroacccrrrraocccrrcrrccorooccrocacckcrcrrrrrrkrrccrcoacrcorcrooccacorcrccccoocroacroraoaarcoorrcrcccccocrrcoccarrorccccrcraoocrrrcoaoroccooccororrrccrcrocrrcorooocorarccoccocrrrocaccrooaaarrcrarooaarrarrororrcrcckracaccorarorocacrrarorrraoacrcokcarcoccoorcrrkaocorcrcrcrooorrcrroorkkaaarkraroraraarooccrkcrcraocooaoocraoorrrccoaraocoorrcokrararrkaakaooroorcororcaorckrrooooakcarokokcoarcccroaakkrrororacrkraooacrkaraoacaraorrorrakaokrokraccaockrookrokoororoooorroaoaokccraoraraokakrookkroakkaookkooraaocakrkokoraoarrakakkakaroaaocakkarkoocokokkrcorkkoorrkraoorkokkarkakokkkracocoaaaaakaraaooraokarrakkorokkoakokakakkcracarcaoaaoaoorcaakkraooaoakkrrroaoaoaarkkarkarkrooaookkroaaarkooakarakkooaokkoorkroaaaokoarkorraoraorcokokaakkaakrkaaokaaaroarkokokkokkkoakaaookkcakkrakooaooroaaaaooaooorkakrkkakkkkaokkooaakorkaroaorkkokaakaaaaaocrrkakrooaaroroakrakrkrakaoaaakokkaaoakrkkoakocaookkakooorkakoaaaaakkokakkorakaaaaoaarkokorkakokakckckookkraooaakokrrakkrkookkaaoakaaaokkaokkaaoakarkakaakkakorkaakkakkkakaaoaakkkaoaokkkakkkoaroookakaokaakkkkkkakoaooakcokkkrrokkkkaoakckakokkocaokaakakaaakakaakakkkkrakoaokkaakkkkkokkkkkkkkrkakkokkroaakkakaoakkoakkkkkkakakakkkaakkkkakkkrkoak"), 229)


# Q4, see Q1420
