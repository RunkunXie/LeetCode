from heapq import *


def merge3list(l1, l2, l3):
    h = []

    idx = [0, 0, 0]
    leng = [len(l1), len(l2), len(l3)]
    ans = []

    heappush(h, (l1[0], 0, 0))
    heappush(h, (l2[0], 1, 0))
    heappush(h, (l3[0], 2, 0))

    while h:

        # pop
        next_num, list_id, cur_idx = heappop(h)

        # next number
        ans.append(next_num)

        # push
        cur_idx += 1
        if cur_idx < leng[list_id]:
            idx[list_id] = cur_idx

            if list_id == 0:
                heappush(h, (l1[cur_idx], 0, cur_idx))
            elif list_id == 1:
                heappush(h, (l2[cur_idx], 1, cur_idx))
            else:
                heappush(h, (l3[cur_idx], 2, cur_idx))

    return ans


print(merge3list([1, 4, 7], [2, 5, 8], [3, 9, 11]))


def merge3list_iter(l1, l2, l3):
    h = []

    idx = [0, 0, 0]
    leng = [len(l1), len(l2), len(l3)]
    ans = []

    heappush(h, (l1[0], 0, 0))
    heappush(h, (l2[0], 1, 0))
    heappush(h, (l3[0], 2, 0))

    while h:

        # pop
        next_num, list_id, cur_idx = heappop(h)

        # next number
        yield next_num

        # push
        cur_idx += 1
        if cur_idx < leng[list_id]:
            idx[list_id] = cur_idx

            if list_id == 0:
                heappush(h, (l1[cur_idx], 0, cur_idx))
            elif list_id == 1:
                heappush(h, (l2[cur_idx], 1, cur_idx))
            else:
                heappush(h, (l3[cur_idx], 2, cur_idx))

    return ans


a = merge3list_iter([1, 4, 7], [2, 5, 8], [3, 9, 11])
print(list(a))

b = merge3list_iter([1, 4, 7], [2, 5, 8], [3, 9, 11])
print(next(b))
print(list(b))
