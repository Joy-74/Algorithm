def optimal_tripartition(A):
    input_list = A
    output_res = [[], [], []]
    n = len(input_list)
    if n <= 3:
        if n == 1:
            if (input_list[0] % 3 == 0):
                output_res[2].append(input_list[0])
            else:
                output_res[1].append(input_list[0])
        elif n == 2:
            output_res = [[input_list[0]], [], [input_list[1]]]
        elif n == 3:
            output_res = [[input_list[0]], [input_list[1]], [input_list[2]]]
        return output_res

    mid = n // 2
    end1 = mid // 2
    output_res = [input_list[0:end1], input_list[end1:mid], input_list[mid:]]
    return output_res

in_file = open("data_b.txt", "r")
lines = in_file.readlines()
in_file.close()
out_file = open("submission_b.txt", "w")
for line in lines:
    line = line.replace(',', ' ').replace('[', '').replace(']', '').replace('(', '').replace(')', '')
    a = list(map(int, line.split()))
    out_file.write(str(optimal_tripartition(a)) + '\n')
out_file.close()  # 关闭输出文件
