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
    a = A[len(A) // 2]
    return a


# In groups of 5 elements (the last array may be less than 5 elements)
# Get the median value, all the median values are stored in an array and returned as the value
def medians_of_quintets(A):
    # array of all medians
    R = []
    # 0-(n-1)，i+5 each time
    for i in range(0, len(A), 5):
        # Get a set
        B = A[i:i + 5]
        # The median value of the current array
        x = median_of_few(B)
        # Append median to array
        R.append(x)
    # Returns an array of all median values
    return R


# Open file in read mode (input)
in_file = open("data_b.txt", "r")
# Get all lines
lines = in_file.readlines()
in_file.close()  # Close input file

# Open file in write mode (output)
out_file = open("submission_b.txt", "w")
# Access all rows sequentially
for line in lines:
    # Remove useless symbols from lines
    line = line.replace(',', ' ').replace('[', '').replace(']', '')
    # Convert to integer array
    A = list(map(int, line.split()))
    # Call median_of_few() and write the result to a file
    out_file.write(str(medians_of_quintets(A)) + '\n')
out_file.close()  # Close output file
