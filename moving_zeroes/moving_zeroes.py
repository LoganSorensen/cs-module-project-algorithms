'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # initialize an empty array to hold any value that equals 0
    zeroArr = []
    i = 0

    while i < len(arr):
        # if the value of the current index is 0, adds it to the zeroArr and
        # removes it from the current array

        # the pointer isn't moved in case the following index
        # (which then becomes the current index) is also a zero
        if arr[i] == 0:
            zeroArr.append(arr[i])
            arr.remove(arr[i])
        # if it isn't zero, the pointer is moved to the next element
        else:
            i += 1

    # once the above loop is finished, every element from the zeroArr is appended
    # to the current array
    for i in zeroArr:
        arr.append(i)

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
