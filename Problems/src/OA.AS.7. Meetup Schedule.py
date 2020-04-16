import heapq


def f(arrival, departure):
    """online dfs sol, maybe incorrect, but pass OA"""
    # visited = set()
    # f.res = 0
    #
    # def dfs(idx, path):
    #     f.res = max(f.res, path)
    #     for i in range(idx, len(arrival)):
    #         for j in range(arrival[i], departure[i] + 1):
    #             if j not in visited:
    #                 visited.add(j)
    #                 dfs(idx + 1, path + 1)
    #                 visited.remove(j)
    #
    # dfs(0, 0)
    # return f.res

    """online greedy sol, correct, didn't pass OA"""
    events = [[arrival[i], departure[i]] for i in range(len(arrival))]
    heapq.heapify(events)
    n = day = 0
    while events:  # make sure taking the upcoming, shorestest-lasting event available from 'day'
        [s, t] = heapq.heappop(events)
        # attend this event on the s-th day
        day = s + 1  # need to increment 'day'
        n += 1  # event attended + 1
        while events and events[0][0] < day:  # update other events' available times, to start no earlier than 'day'
            [c, d] = heapq.heappop(events)
            if day <= d:
                heapq.heappush(events, [day, d])
    return n


print(f([1, 2, 2, 3], [2, 2, 3, 4]), 4)
print(f([2, 2, 2, 3], [2, 2, 3, 4]), 3)
print(f([1, 2, 3, 3], [3, 2, 3, 4]), 4)

print(f([1, 1, 1, 1, 1], [2, 2, 2, 2, 6]), 3)
print(f([2, 1, 3, 1, 1], [2, 2, 3, 5, 5]), 5)
print(f([1, 1, 1, 2, 2], [5, 5, 5, 3, 3]), 5)
print(f([1, 2, 1, 2, 2], [5, 5, 4, 3, 3]), 5)
