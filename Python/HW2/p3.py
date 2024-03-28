def partition_at(A, k):
    a = []  # A<
    b = []  # A>
    for x in A:
        # x is the current element
        if x < k:
            # elements that belong to A<
            a.append(x)
        elif x > k:
            # elements that belong to A>
            b.append(x)
    # return a and b
    return (a, b)


# Open file in read mode (input)
in_file = open("data_c.txt", "r")
# Get all rows
lines = in_file.readlines()
in_file.close()  # Close input file

# Open file in write mode (output)
out_file = open("submission_c.txt", "w")
# Access all rows sequentially
for line in lines:
    # Remove useless symbols from lines
    line = line.replace(',', ' ').replace('[', '').replace(']', '').replace('(', '').replace(')', '')
    # Convert to integer array
    A = list(map(int, line.split()))
    # k is the last element in the array
    k = A[len(A) - 1]
    # remove the last element, it doesn't count as an element in the array
    A.pop()
    # call partition_at() to write each set of A< and A> bounded by k to the file
    out_file.write(str(partition_at(A, k)) + '\n')
out_file.close()  # Close output file


