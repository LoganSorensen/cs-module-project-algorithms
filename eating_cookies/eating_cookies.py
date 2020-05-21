'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, current=0):
    # print(n,current)
    if current > n:
        return 0
    if current == n:
        return 1
    return eating_cookies(n, current+1) + eating_cookies(n, current+2) + eating_cookies(n, current+3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
