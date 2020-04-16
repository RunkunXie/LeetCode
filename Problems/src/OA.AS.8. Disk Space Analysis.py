
def segment(x, space):
    # Write your code here

    # special case 1
    if not space:
        return None

    # special case 2
    if x == 1:
        return max(space)

    # store min element
    left = []
    right = []
    min_element = []

    # left[i]: minimum of block start to nums[i]
    for i, v in enumerate(space):

        if i % x == 0:
            block_min = v
            left.append(v)
        else:
            if v < block_min:
                left.append(v)
                block_min = v
            else:
                left.append(block_min)

    # right[i]: minimum of nums[i] to block end
    block_min = space[-1]
    for i in range(len(space) - 1, -1, -1):

        v = space[i]

        if i % x == x - 1:
            block_min = v
            right.append(v)
        else:
            if v < block_min:
                right.append(v)
                block_min = v
            else:
                right.append(block_min)
    right.reverse()

    # calc min_element
    for i in range(x - 1, len(space)):

        if i % x == x - 1:
            min_element.append(left[i])
        else:
            min_element.append(min(left[i], right[i - x + 1]))

    return max(min_element)
