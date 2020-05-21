'''
Input: a List of integers
Returns: a List of integers
'''
import math

def product_of_all_other_numbers(arr):
    productArr=[]
    i = 0

    while i < len(arr):
        # get values before the current index
        before = arr[:i]
        # get values after the current index
        after = arr[i+1:]
        # concatenate both arrays
        newArr = before + after
        # append the product of the new array's values to the productArr
        productArr.append(math.prod(newArr))
        i += 1
    return productArr

# # original implementation
# def product_of_all_other_numbers(arr):
#     product = 1
#     zeroProduct = 1
#     # calculates the product of every element in the array
#     for i in arr:
#         # if an element is not equal to zero, multiply it
#         if i != 0:
#             product *= i
#             zeroProduct *= i
#         else:
#             product *= i
#             zeroProduct *= 1

#     newArr = []
#     # divides the product by each element in the array to find the product
#     # of every other element
#     for i in arr:
#         if i != 0:
#             newArr.append(product//i)
#         else:
#             newArr.append(zeroProduct)

#     # print(newArr)
#     return newArr


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [7, 9, 1, 8, 6, 0, 7, 8, 8, 7, 10]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
