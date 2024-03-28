# Homework 1 problem 6
# Written by Jiayu Li

def f(A):
    cnt = 0
    # 0 ~ n-2
    for i in range(0, len(A) - 1):
        a = A[i]
        b = A[i + 1]
        if a > b:
            continue
        if a * a == b:
            cnt += 1
    return cnt


# open file in read mode
file = open('data.txt', 'r')
# open output file in write mode
output_file = open('submission.txt', 'w')

# Get all lines of a file
lines = file.readlines()
# iterate
# line refers to each line of the file
for line in lines:
    # Convert segmented text to integer
    # then turn into a list
    A = list(map(int, line.split()))
    # call function f and get the result
    cnt = f(A)
    # print the result for each line
    output_file.write(str(cnt) + '\n')
    print(cnt)

# Close file
file.close()
output_file.close()
