'''
数值的整数次方
考虑：
输入的是整数，负数，零
'''
# def double_power(n):
#     """
#     求一个数的整数次方
#     :param n:
#     :return:
#     """

class Solution:
    def Power(self, base, exponent):
        """
        实现函数的整数次方，、
        考虑很多情况
        先把乘方后的值算出来，
        在根据输入的数字的正负号，进行判断
        :param base:
        :param exponent:
        :return:
        """

        if base == 0:
            return False
        if exponent == 0:
            return 1

        res = 1.0
        for i in range(1, abs(exponent) + 1):
            res *= abs(base)


        if exponent < 0:
            if base > 0:
                return 1 / res
            else:
                return - 1 / res
        else:
            if base > 0:
                return res
            else:
                return -res



















        # if base == 0:
        #     return  False
        # if exponent == 0:
        #     return 1
        # res = 1.0
        # for i in range(1, abs(exponent) + 1):
        #     res *= abs(base)
        #
        # if exponent < 0:
        #     if base > 0:
        #         return 1 / res
        #     else:
        #         return -1 / res
        # else:
        #     if base > 0:
        #         return res
        #     else:
        #         return -res



