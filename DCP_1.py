'''
Daily Coding Problem #1:
Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def can_two_add_to(k, l):
    for i in l:
        for j in l[1:]:
            print(f"i: {i}, j: {j}")
            if i + j == k:
                return True
    return False

if __name__ == "__main__":
    my_list = [10, 15, 3, 7]
    k = 15
    can_two_add_to(k, my_list)