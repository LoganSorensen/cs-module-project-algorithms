'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=0):
    if n == 0: 
        return 1
    elif n < 0:
        return 0
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = [0 for _ in range(n+1)]
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]
    # Original implementation:
    # if current > n:
    #     return 0
    # if current == n:
    #     return 1
    # return eating_cookies(n, current+1) + eating_cookies(n, current+2) + eating_cookies(n, current+3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
