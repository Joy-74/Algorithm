# Selection sort
def selection_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A


def median_of_few(A):
    # Call the implemented sort function
    selection_sort(A)
    # Get the middle element
    # //means divisible e.g. 5//2 = 2
    a = A[len(A) // 2]
    return a


# Open file in read mode (input)
in_file = open("data_a.txt", "r")
# Get all lines
lines = in_file.readlines()
in_file.close()  # Close input file

# Open file in write mode (output)
out_file = open("submission_a.txt", "w")
# Access all rows sequentially
for line in lines:
    # Remove useless symbols from lines
    line = line.replace(',', ' ').replace('[', '').replace(']', '')
    # Convert to integer array
    A = list(map(int, line.split()))
    # Call median_of_few() and write the result to a file
    out_file.write(str(median_of_few(A)) + '\n')
out_file.close()  # Close output file
