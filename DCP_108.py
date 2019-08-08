'''
Daily Coding Problem #108:
Given two strings A and B, return whether or not A can be shifted some number
of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is 
acb, return false.
'''
def can_shift(arg1, arg2):
    for i in range(len(arg1)):
        # Make all iterations here
        shifted = arg1[-i:] + arg1[:-i]
        if shifted == arg2:
            return True
    return False

if __name__ == "__main__":
    res1 = can_shift("abcde", "cdeab")
    res2 = can_shift("abcde", "cddeab")

    if res1 == True and res2 == False:
        print("Success.")
    else:
        print("Failed.")