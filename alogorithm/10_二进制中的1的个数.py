''''''
'''
请实现一个函数，输入一个整数，输出该整数的二进制表示中1的个数
例如：9表示成二进制时1001， 有2位是1， 因此输入9 输出2

思路：
    先判断二进制表示中最右边是不是1，
    接着把输入的整数右移一位，再判断是不是1
    这样每移动一位进行判断
    直到整数变成0
'''

# class Solution:
    # def Number_of_1(self, n):
    #     if n < 0:
    #         n  = n & 0xffffffff
    #
    #     count = 0
    #     while n:
    #         if n & 1:
    #             count += 1
    #         n = n >> 1
    #     return count
    #     # print(n)



class Solution:
    def Num_of_1(self, n):
        if n < 0:
            n = n & 0xffffffff
        count = 0
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count



# s = Solution()
# print(s.Number_of_1(9))

print(9 & 1)