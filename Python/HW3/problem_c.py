def greedy_knapsack(pair_array, w):
    (max_diff_val_value, max_diff_val_weight) = pair_array[0]
    max_diff_val = max_diff_val_value / max_diff_val_weight
    max_diff_index = 0

    for i in range(1, len(pair_array)):
        (val, weight) = pair_array[i]
        if val / weight > max_diff_val:
            max_diff_val = val / weight
            max_diff_index = i

    output = []
    max_diff_pair = pair_array[max_diff_index]
    (max_diff_val_value, max_diff_val_weight) = max_diff_pair

    if max_diff_val_weight <= w:
        if max_diff_val_value + max_diff_val_weight == w or max_diff_val_weight == w:
            output = [max_diff_pair] * len(pair_array)
        else:
            while w >= max_diff_val_weight:
                output.append(max_diff_pair)
                w -= max_diff_val_weight

            for i in range(len(pair_array)):
                x = pair_array[i]
                (current_val, current_weight) = x
                if current_weight == w:
                    output.append(x)
                    w -= current_weight
                    return output
            output.append(max_diff_pair)
    return output

in_file = open("data_c.txt", "r")
lines = in_file.readlines()
in_file.close()
out_file = open("submission_c.txt", "w")
for line in lines:
    line = line.replace(',', ' ').replace('[', '').replace(']', '').replace('(', '').replace(')', '')
    a = list(map(int, line.split()))
    w = a[len(a) - 1]
    a.pop()
    pair_list = []
    for i in range(0, len(a), 2):
        pair_list.append((a[i], a[i+1]))
    out_file.write(str(greedy_knapsack(pair_list, w)) + '\n')
out_file.close()
