'''
Daily Coding Problem #109:
Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd
bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
'''

import sys

def swap_bits(bnum):
    r1 = (bnum << 1) & 0b10101010
    r2 = (bnum >> 1) & 0b01010101
    res = r1 | r2
    return res

if __name__ == "__main__":    
    arg = 0b11100010
    res = swap_bits(arg)
    print(bin(res))
