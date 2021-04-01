def find_max(input):
    max = input[0]
    for i in range(1, len(input)):
        if input[i] >= max:
            max = input[i]
    return max


# Brute force: O(n^2)
def brute_force(input):
    max_sum = - 10000
    for i in range(len(input)):
        for j in range(i, len(input)):
            cur_sum = sum(input[i:(j + 1)])
            if cur_sum > max_sum:
                max_sum = cur_sum
                left_index = i
                right_index = j
    return [left_index, right_index, max_sum]


# Divide-Conquer: O(nlgn)
def find_max_crossing(input, l, m, h):
    left_sum = right_sum = -10000
    sum = 0
    for i in range(m, l - 1, -1):
        sum = sum + input[i]
        if sum > left_sum:
            left_sum = sum
            left_index = i
    sum = 0
    for j in range(m + 1, h + 1):
        sum = sum + input[j]
        if sum > right_sum:
            right_sum = sum
            right_index = j

    return [left_index, right_index, left_sum + right_sum]


def divide_conquer(input, l=0, h=len(input) - 1):
    if l == h:
        return [l, h, input[l]]
    else:
        m = round((l + h) / 2 - 0.5)
        [left_l, left_h, left_sum] = divide_conquer(input, l, m)
        [right_l, right_h, right_sum] = divide_conquer(input, m + 1, h)
        [cross_l, cross_h, cross_sum] = find_max_crossing(input, l, m, h)

        max_sum = find_max([left_sum, right_sum, cross_sum])
        if left_sum == max_sum:
            return [left_l, left_h, left_sum]
        elif right_sum == max_sum:
            return [right_l, right_h, right_sum]
        else:
            return [cross_l, cross_h, cross_sum]


def kadane(input):
    # Kadane: O(n)
    local_max = global_max = input[0]
    left_index = 0
    right_index = 0
    for i in range(1, len(input)):
        if input[i] > input[i] + local_max:
            local_max = input[i]
            left_index = i
        else:
            local_max = input[i] + local_max
        if global_max < local_max:
            global_max = local_max
            right_index = i

    return [left_index, right_index, global_max]


if __name__ == '__main__':
    import random

    input = random.sample(range(-50, -10), 10)
    print(brute_force(input))
    print(divide_conquer(input))
    print(kadane(input))
