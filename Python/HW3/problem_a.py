import sys


def factor(x):
    a = []
    i = 2
    while i <= x // 2:
        if x % i == 0:
            a.append(i)
        i += 1
    return a


def optimal_change(a, n):
    b = a
    b.sort()
    size = len(b)

    r1 = []
    r2 = []

    # Case 1: There are factors in the array
    f = factor(n)
    for x in f:  # iterate over all factors
        if x in a:  # There is this factor in the array
            r1 = [x] * (n // x)  # The quotient is the number and the factor x is the element in the result

    # Case 2: The largest number in the array takes precedence, so that n keeps decreasing
    for i in range(size - 1, -1, -1):
        if n == 0:
            break

        number = b[i]
        while n >= number:
            n -= number
            r2.append(number)

    # decision making:
    # If one and the array are empty, let the array be optimal
    if len(r1) == 0:
        return r2
    else:
        # If the length of the result of the factorial solution is less than or equal to the
        # length of the result of the largest-first solution
        # Take the result of the factorial solution, r1 is the result of the factorial solution,
        # and r2 is the result of the larger value first solution
        return r1 if len(r1) <= len(r2) else r2


# Open file in read mode (input)
in_file = open("data_a.txt", "r")
# get all rows
lines = in_file.readlines()
in_file.close()  # close input file

# Open file in write mode (output)
out_file = open("submission_a.txt", "w")
# access all rows sequentially
for line in lines:
    # Remove useless symbols from lines
    line = line.replace(',', ' ').replace('[', '').replace(']', '').replace('(', '').replace(')', '')
    # Convert to integer array
    a = list(map(int, line.split()))
    # n is the last element in the array
    n = a[len(a) - 1]
    # remove the last element, it doesn't count as an element in the array
    a.pop()
    # call partition_at() to write each set of A< and A> bounded by k to the file
    out_file.write(str(optimal_change(a, n)) + '\n')
out_file.close()  # close output file
