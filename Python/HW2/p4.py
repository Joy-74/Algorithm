# Selection sort
import sys


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
        # The median value of the current array
        B = A[i:i + 5]
        x = median_of_few(B)
        # Append median to array
        R.append(x)
    # Returns an array of all median values
    return R


# A<, A>
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


# 0 1 1 2 3 , k=2
# output: 1
def quickselect(A, i):
    n = len(A)
    if n == 1:
        return A[0]
    B = A
    B.sort()
    return B[i]


in_file = open("data_d.txt", "r")
lines = in_file.readlines()
in_file.close()

out_file = open("submission_d.txt", "w")
for line in lines:
    line = line.replace(',', ' ').replace('[', '').replace(']', '').replace('(', '').replace(')', '')
    A = list(map(int, line.split()))
    k = A[len(A) - 1]
    A.pop()
    out_file.write(str(quickselect(A, k)) + '\n')
out_file.close()
