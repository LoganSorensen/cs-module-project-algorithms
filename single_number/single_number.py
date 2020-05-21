'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    counts = {}

    for x in arr:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    for num in counts:
        if counts[num] == 1:
            return num
    # Original implementation
    # for i in range(len(arr)):
    #     found_twice = False

    #     for j in range(len(arr)):
    #         if i != j and arr[i] == arr[j]:
    #             found_twice = True
    #     if not found_twice:
    #         return arr[i]
    # return -1


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
